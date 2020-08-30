import threading
import logging
import multiprocessing
import yaml
from gensim.models import KeyedVectors

from generate_set import read_word_set

try:
    print("Loading config.yml...")
    config_yaml = open("../../config.yml")
    print("config.yml loaded")
except:
    exit("config.yml file is missing, run setup.py")

CONFIG = yaml.safe_load(config_yaml)

try:
    print("Loading Word2Vec model...")
    word_vector = KeyedVectors.load_word2vec_format(
        "../wikipedia-vector.bin", binary=True)
    print("Word2Vec model loaded")
except:
    exit("Word2Vec model is missing, run train_model.sh")


def get_arrays(word_set, total_words, result_list, index, lock):
    dimension_count = CONFIG["word2vec"]["vector"]["dimension"]
    min_array = [9999] * dimension_count
    max_array = [-9999] * dimension_count

    i = 0
    for word in word_set:
        try:
            word = word.split()[0]
        except:
            i += 1
            continue

        if (i % 25000 == 0):
            print("Thread {}: {:.2f}% complete, current word: {}".format(
                index + 1, 100 * i/total_words, word))
        try:
            v = word_vector[word].tolist()
            if len(v) == dimension_count:
                for j in range(dimension_count):
                    if v[j] > max_array[j]:
                        max_array[j] = v[j]
                    if v[j] < min_array[j]:
                        min_array[j] = v[j]
        except:
            pass
        i += 1
    lock.acquire()
    result_list[index] = (min_array, max_array)
    lock.release()


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def run():
    cores = multiprocessing.cpu_count()
    word_set, cnt = read_word_set()

    res = [[]] * cores
    split_sets = list(split(list(word_set), cores))

    threads = []
    lock = threading.Lock()
    print("Running on " + str(cores) + " threads")

    for i in range(cores):
        thread = threading.Thread(target=get_arrays, args=(
            split_sets[i], cnt/cores, res, i, lock))
        print("Thread {} created".format(i + 1))
        threads.append(thread)
        thread.start()

    for index, thread in enumerate(threads):
        thread.join()
        print("Thread {} completed".format(index + 1))

    min_array = res[0][0][:]
    max_array = res[0][1][:]
    for i in range(cores):
        for j in range(CONFIG["word2vec"]["vector"]["dimension"]):
            if res[i][1][j] > max_array[j]:
                max_array[j] = res[i][1][j]
            if res[i][0][j] < min_array[j]:
                min_array[j] = res[i][0][j]

    return list(zip(min_array, max_array))


if __name__ == "__main__":
    limits = run()

    boundaries = []
    for e in limits:
        boundaries.append({"min": e[0], "max": e[1]})
    CONFIG["word2vec"]["vector"]["boundaries"] = boundaries

    try:
        with open("../../config.yml", "w") as file:
            yaml.dump(CONFIG, file)
        print("Boundary values saved to config.yml")
    except:
        print("Error saving boundary values to config.yml, check permissions")

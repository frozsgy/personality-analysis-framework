import requests
import json
import threading
import logging
import multiprocessing
import yaml

from generate_set import read_word_set

try:
    config_yaml = open("../../config.yml")
except:
    exit("config.yml file is missing, run setup.py")

CONFIG = yaml.safe_load(config_yaml)

def get_arrays(word_set, total_words, result_list, index, lock):
    dimension_count = CONFIG["word2vec"]["vector"]["dimension"]
    min_array = [9999] * dimension_count
    max_array = [-9999] * dimension_count
    base_url = CONFIG["word2vec"]["service"]["url"] + ":" + str(CONFIG["word2vec"]["service"]["port"]) + "/word2vec?word="

    i = 0
    for word in word_set:
        try:
            link = base_url + word.split()[0]
        except:
            i += 1
            continue
        req = requests.get(link)
        if (i % 10000 == 0):
            print("%" + str(100 * (float(i)/total_words)) + " DONE - Handling word nr: " + str(i) + " (" + word.split()[0] + ")")
            print(min_array)
            print(max_array)
        try:
            v = req.json()['word2vec']            
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

    for i in range(cores):
        thread = threading.Thread(target=get_arrays, args=(split_sets[i], cnt/cores, res, i, lock))
        threads.append(thread)
        thread.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

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

    with open("../../config.yml", "w") as file:
        yaml.dump(CONFIG, file)
    


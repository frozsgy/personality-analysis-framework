import requests
import json


def create_word_set():
    word_set = set()
    print("Reading words from word set...")
    with open("word-set.txt") as fp:
        for cnt, line in enumerate(fp):
            if cnt % 100000 == 0:
                print("Read " + str(cnt) + " lines")
            word_set.add(line)
    print("Reading from word set is complete!")
    return (word_set, cnt)

def get_arrays(word_set, total_words, dimension_count):
    min_array = [9999] * dimension_count
    max_array = [-9999] * dimension_count
    base_url = "http://127.0.0.1:5000/word2vec?word="

    i = 0

    for word in word_set:
        link = base_url + word.split()[0]
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
    return (min_array, max_array)


if __name__ == "__main__":
    word_set, cnt = create_word_set()
    min_array, max_array = get_arrays(word_set, cnt, 38)
    print("min array:")
    print(min_array)
    print("max_array:")
    print(max_array)



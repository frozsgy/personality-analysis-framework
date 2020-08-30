import sys
from gensim.corpora import WikiCorpus

def make_corpus(in_f):

    print('Generating dictionary from Wikipedia corpus...')
    output = open("word-list.txt", 'w')
    wiki = WikiCorpus(in_f)

    i = 0
    for text in wiki.get_texts():
        output.write(bytes('\n'.join(text), 'utf-8').decode('utf-8') + '\n')
        i = i + 1
        if (i % 10000 == 0):
            print('Processed ' + str(i) + ' articles')
    output.close()
    print('Processing complete!')


def make_set():
    word_set = set()
    filepath = "word-list.txt"

    print("Reading words from word list...")
    with open("word-list.txt") as fp:
        for cnt, line in enumerate(fp):
            if cnt % 100000 == 0:
                print("Read " + str(cnt) + " lines")
            word_set.add(line)

    print("Reading from word list is complete!")
    print("Writing to word set file...")
    with open("word-set.txt", "w") as output:
        output.write(''.join(word_set))

    print("Writing to word set is complete!")


def read_word_set():
    word_set = set()
    print("Reading words from word set...")
    with open("word-set.txt") as fp:
        for cnt, line in enumerate(fp):
            if cnt % 100000 == 0:
                print("Read " + str(cnt) + " lines")
            word_set.add(line)
    print("Reading from word set is complete!")
    return (word_set, cnt)


if __name__ == '__main__':

    make_corpus("../trwiki-latest-pages-articles.xml.bz2")
    make_set()

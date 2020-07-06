# uses the stopword list from nltk module

class StopWord:
    __dictionary = []

    def __init__(self):
        with open("turkish_stopwords_nltk", 'r', encoding = 'utf-8') as fdict:
            for line in fdict:
                self.__dictionary.append(line.strip())


    def is_stop_word(self, word):

        return word in self.__dictionary
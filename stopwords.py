# uses the stopword list from the article
# https://www.ranks.nl/stopwords/turkish

class StopWord:
    __dictionary = []

    def __init__(self):
        with open("ranks-nl-stopwords", 'r', encoding = 'utf-8') as fdict:
            for line in fdict:
                self.__dictionary.append(line.strip())


    def is_stop_word(self, word):
        return word in self.__dictionary
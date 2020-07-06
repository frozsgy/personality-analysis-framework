# modified and improved version of https://github.com/ahmetax/trstop

class StopWord:
    __dictionary = {}

    def __init__(self):
        with open("derlemtr2016-10000.txt", 'r', encoding = 'utf-8') as fdict:
            for line in fdict:
                if (line[0] not in ['0', '1']):
                    continue
                freq, word = line.strip().split()
                self.__dictionary[word] = int(freq)

    def is_stop_word(self, word):
        """ 
        parametre olarak verilen sozcugun sozlukte olup olmadigini kontrol eder.
        checks if word is in the dictionary, returns true if so.

        word: str
        return: bool
        """
        return word in self.__dictionary.keys()


    def get_word_freq(self, word):
        """
        parametre olarak verilen sozcugun frekansini geri dondurur. 
        sozcuk sozlukte yoksa 0 dondudur.
        returns usage frequency of word. returns 0 if word is not in the dict.

        word: str
        return: int
        """
        if is_stop_word(word):
            return self.__dictionary[word]
        else:
            return 0

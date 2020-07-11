import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), '..')))

import re
import string


from utils.stopwords import * 
#from twitter.turkish import * 

def preprocess(text):
    # removing line breaks
    text = text.replace('\n', ' ').replace('\r', '')
    
    # removing the hashtag sign
    text = text.replace("#", "")
    #debug("removed hashtags: \n" + text)

    # removing the RT keyword that gets added automatically when a RT'd tweet is fetched via the API
    # RT @username: original_tweet
    regex = r"^RT @[A-Za-z0-9_]{1,}: (.*?)$"
    rt_search = re.search(regex, text, flags=re.S)
    if rt_search:
        rts = rt_search.groups()
        text = rts[0]
    #debug("removed RT's: \n" + text)

    # removing mentions
    # username details: https://help.twitter.com/en/managing-your-account/twitter-username-rules
    # username limit: 15 chars
    # [A-Za-z], [0-9], [_]
    # regex for mentions => @[A-Za-z0-9_]{1,15}
    # this is a bit tricky because if we remove everything starting with @, we might remove non-valid usernames as well.
    # removing mentions without the username length restriction
    regex = r"@[A-Za-z0-9_]{1,}"
    text = re.sub(regex, '', text)
    #debug("removed mentions: \n" + text)


    #tr_text = TurkishText(text)
    #text = tr_text.lower() -- zemberek handles this

    # TODO -- BUGGY
    # twitter uses t.co for url's so we can use a regex to match that only if the api gets stuff with t.co 
    # for example https://t.co/BLABLA
    # removing URL's 
    #regex = r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-z]{2,8}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    regex = r"(http(s)?:\/\/t.co\/)[a-zA-Z0-9]+"
    text = re.sub(regex, '', text)
    #debug("removed URL's: \n" + text)


    # remove punctuation
    #text.translate(str.maketrans('', '', string.punctuation))
    #text = text.replace("'", "") # odtü'lü gibi kelimeler için -> bundan emin olamadım?
    #text = text.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    #text = text.replace("…", "")
    #debug("removed punctuation: \n" + text)

    # remove numbers ? or convert them to words
    # -- TODO --

    # remove stopwords
    # -- TODO -- 
    # https://github.com/ahmetax/trstop

    # remove extra whitespace
    # method 1: regex --> leaves extra whitespace at the beginning or the end, might need trim
    #regex = r"\s+"
    #text = re.sub(regex, ' ', text)

    # method 2: 
    #text = ' '.join(text.split())
    #text = re.sub(" \d+", " ", text)

    # method 3: method 2 merged with stopword removal:
    s = StopWord()
    s_s = text.split()
    r = [i for i in s_s if s.is_stop_word(i) is False]
    text = ' '.join(r)
    #debug("removed whitespace and stopwords: \n" + text)
    return text


if __name__ == '__main__':

    text = "RT @ODTUKuzeyKibris: Aynı gökyüzü altında ama birbirinden uzak ODTÜ'lülere; https://t.co/Y9MWOCdvgY via @YouTube"
    #text = "Teknofest 2020'ye çeşitli yarışma kategorilerinde 74 takım ve 231 öğrenci ile katılıyoruz. @teknofest #ODTÜ #METU… https://t.co/xkU6UPr2gU"
    #text = "RT @BirGun_Gazetesi: AKP'li isimden, Sivas Katliamı'na 'Sivas Katliamı' diyenler hakkında suç duyurusu: \"\"Sivas'ın imajını zedeliyorlar\"\"\n htt…" 

    #text = input()
    print("input: \n" + text + "\n" + "-" * 80)
    tt = preprocess(text)
    print("output: \n" + tt + "\n" + "-" * 80)


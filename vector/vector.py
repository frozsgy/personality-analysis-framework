#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

class Vector:
    
    # time-related
    __morning = 0
    __afternoon = 0
    __evening = 0
    __night = 0
    
    # zemberek related
    __word = 0
    __verb = 0
    __noun = 0
    __punctuation = 0
    __adjective = 0
    __adverb = 0
    __negative = 0
    __numeral = 0
    __determiner = 0
    __conjunction = 0
    __pronoun = 0
    __incorrect = 0
    __plural = 0
    __full_stop = 0

    # emoji
    __smiling_emoji = 0
    __negative_emoji = 0


    def __init__(self):
        pass

    def get_vector(self):
        return [self.__morning, self.__afternoon, self.__evening, self.__night, self.__word, self.__verb, self.__noun, self.__punctuation, self.__adjective, self.__adverb, self.__negative, self.__numeral, self.__determiner, self.__conjunction, self.__pronoun, self.__incorrect, self.__plural, self.__full_stop, self.__smiling_emoji, self.__negative_emoji]

    def set_time(self, tweet):
        tweet_time = tweet.get_time()
        date_obj = datetime.strptime(tweet_time, "%Y-%m-%d %H:%M:%S")
        hour = date_obj.hour // 6

        if hour == 0:
            # night
            self.__evening += 1
            self.__night += 1
        elif hour == 1:
            # morning
            self.__night += 1
            self.__morning += 1
        elif hour == 2:
            # afternoon
            self.__morning += 1
            self.__afternoon += 1
        else :
            # evening
            self.__afternoon += 1
            self.__evening += 1

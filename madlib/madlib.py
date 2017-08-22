# -*- coding: utf-8 -*-
# @Time      : 022/8/22/17 9:11 PM
# @Author    : Hooper Chao
# @File      : madlib
# @Created by: PyCharm
from random import randint


def random_verb():
    random_num = randint(0,1)
    if random_num == 1:
        return 'run'
    else:
        return 'walk'


def random_noun():
    random_num = randint(0,1)
    if random_num == 1:
        return 'company'
    else:
        return 'road'


def word_transformer(word):
    if word == 'VERB':
        return random_verb()
    elif word == 'NOUN':
        return random_noun()
    else:
        return word[0]


def processor(madlib):
    processed = ''
    index = 0
    box_length = 4
    while index < len(madlib):
        add_to = word_transformer(madlib[index:index + box_length])
        processed += add_to
        if len(add_to) == 1:
            index += 1
        else:
            index += 4
    return processed


string1 = 'I am VERBing a NOUN.'
string2 = "Don't blame me, you can not VERB that NOUN"

print processor(string1)
print processor(string2)

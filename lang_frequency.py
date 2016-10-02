#!/usr/bin/env python2

import argparse
import operator
import os
import re
import sys


SCRIPT_NAME = 'devmanorg frequent words'

reload(sys)
sys.setdefaultencoding("utf-8")


def load_data(filepath):
    if not os.path.exists(filepath):
        return None

    with open(filepath) as input_file:
        return input_file.read().decode('utf8')


def get_most_frequent_words(text):
    words = re.findall(r'(\w+)', text, re.UNICODE)
    words_stat = dict()

    for word in words:
        if not word.isdigit():
            word = word.lower()
            words_stat[word] = words_stat.get(word, 0) + 1

    words_stat = sorted(
        words_stat.iteritems(),
        key=operator.itemgetter(1),
        reverse=True
    )

    return [w for w, _ in words_stat]


parser = argparse.ArgumentParser(description=SCRIPT_NAME)
parser.add_argument('filename', help='Input file')


if __name__ == '__main__':
    args = parser.parse_args()

    text = load_data(args.filename)
    most_frequent_words = get_most_frequent_words(text)

    print ("\n".join(most_frequent_words[:10]))

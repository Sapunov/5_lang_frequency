#!/usr/bin/env python3

import os
import argparse
import re

from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None

    with open(filepath) as input_file:
        return input_file.read()


def get_most_frequent_words(text, min_length=None):
    words = re.findall(r"(\w+)", text, re.UNICODE)

    words = map(lambda word: word.lower(), words)

    if min_length is not None:
        words = filter(lambda word: len(word) >= min_length, words)

    return Counter(words)


def main():
    description = "Get most frequent words from FILENAME"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        "-f", "--filepath",
        required=True,
        help="File path")
    parser.add_argument(
        "-n",
        help="Number of words to print. Default: 10",
        default=10,
        type=int
    )
    parser.add_argument(
        "-m", "--min-length",
        type=int,
        help="Minimum word length for evaluation. Default: None"
    )
    parser.add_argument(
        "-t", "--tab",
        action="store_true",
        help="TabSeparated format")

    args = parser.parse_args()

    text = load_data(args.filepath)
    most_frequent_words = get_most_frequent_words(text, args.min_length)

    print_format = "{0:<6}{1:<25}{2}"

    amount = args.n or None

    if (args.tab):
        for item in enumerate(most_frequent_words.most_common(amount)):
            print("{0}\t{1}\t{2}".format(
                item[0] + 1,
                item[1][0],
                item[1][1])
            )
    else:
        print(print_format.format("#", "Word", "Freq"))

        for item in enumerate(most_frequent_words.most_common(amount)):
            print(print_format.format(
                item[0] + 1,
                item[1][0].ljust(25, "."),
                item[1][1])
            )


if __name__ == "__main__":
    main()

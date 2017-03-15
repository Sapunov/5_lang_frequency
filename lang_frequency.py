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


is_ascii = lambda string: len(string) == len(string.encode())


def extract_words(text, to_lowercase=False, min_length=None,
    ascii_only=False, symbols_only=False
):

    words = re.findall(r"(\w+)", text, re.UNICODE)

    if ascii_only:
        words = [word for word in words if is_ascii(word)]

    if symbols_only:
        words = [word for word in words if not word.isdigit()]

    if to_lowercase:
        words = [word.lower() for word in words]

    if min_length:
        words = [word for word in words if len(word) >= min_length]

    return words


def get_most_frequent_words(words):

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
        help="TabSeparated format"
    )
    parser.add_argument(
        "-c", "--count",
        action="store_true",
        help="Show only number of words in text"
    )
    parser.add_argument(
        "-cu", "--count_unique",
        action="store_true",
        help="Show only number of unique words in text"
    )
    parser.add_argument(
        "-i", "--ignore-case",
        action="store_true",
        help="Case insensitive"
    )
    parser.add_argument(
        "-a", "--ascii",
        action="store_true",
        help="Work with ascii symbols only"
    )
    parser.add_argument(
        "-s", "--symbols",
        action="store_true",
        help="Work with only sumbols i.e. not numbers"
    )

    args = parser.parse_args()

    text = load_data(args.filepath)
    words = extract_words(
        text,
        args.ignore_case,
        args.min_length,
        args.ascii,
        args.symbols
    )

    if args.count:
        print(len(list(words)))
    else:
        most_frequent_words = get_most_frequent_words(words)

        if args.count_unique:
            return print(len(most_frequent_words))

        amount = args.n or None

        if args.tab:
            for item in enumerate(most_frequent_words.most_common(amount)):
                print("{0}\t{1}\t{2}".format(
                    item[0] + 1,
                    item[1][0],
                    item[1][1])
                )
        else:
            print_format = "{0:<6} {1:<25} {2}"

            print(print_format.format("#", "Word", "Freq"))

            for item in enumerate(most_frequent_words.most_common(amount)):
                print(print_format.format(
                    item[0] + 1,
                    item[1][0].ljust(25, "."),
                    item[1][1])
                )


if __name__ == "__main__":
    main()

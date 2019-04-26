import re
import collections
import argparse
import os


def load_data(filepath):
    with open(filepath, 'rt') as file:
        return file.read()


def get_most_frequent_words(text, amount_out):
    words_text = re.findall(r'\b(?!\d)\w+\b', text)
    return collections.Counter(words_text).most_common(amount_out)

def main():
    AMOUNTOUT = 10

    parser = argparse.ArgumentParser()
    parser.add_argument('pathfile', help='Path to the text file')
    parser.add_argument('-a', '--amount_out', type=int, default=AMOUNTOUT, help='The number of the most frequent words')

    params = parser.parse_args()

    filepath = params.pathfile
    amount_out = params.amount_out

    if not os.path.isfile(filepath):
        exit('File not found')

    text = load_data(filepath).lower()

    frequent_words = get_most_frequent_words(text, amount_out)
    for word, count in frequent_words:
        print('{} : {}'.format(word, count))

if __name__ == '__main__':
    main()

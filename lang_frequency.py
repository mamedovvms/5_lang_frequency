import re
import collections


def load_data(filepath):

    with open(filepath, 'rt') as f:
        return f.read().lower()


def get_most_frequent_words(text):
    words_text = re.findall(r'\b(?!\d)\w+\b', text)
    return collections.Counter(words_text)


if __name__ == '__main__':
    filepath = input('Add path to file: ')
    amount_out = int(input('Amount output: '))
    text = load_data(filepath)
    frequent_words = get_most_frequent_words(text)
    for word, count in get_most_frequent_words(text).most_common(amount_out):
        print(word, ' : ', count)

import re
import collections


def load_data(filepath):

    with open(filepath, 'rt') as f:
        return f.read().lower()


def get_most_frequent_words(text):
    words_text = re.findall(r'\b(?!\d)\w+\b', text)
    return collections.Counter(words_text).most_common(5)


if __name__ == '__main__':
    filepath = input('Add path to file: ')
    text = load_data(filepath)
    for word, count in get_most_frequent_words(text):
        print(word, ' : ', count)

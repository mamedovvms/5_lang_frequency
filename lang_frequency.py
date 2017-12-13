import re


def load_data(filepath):

    with open(filepath, 'rt') as f:
        return f.read().lower()


def get_most_frequent_words(text):
    words_text = re.findall(r'\b(?!\d)\w+\b', text)
    set_words = {word: words_text.count(word) for word in set(words_text)}
    return sorted(set_words.items(), key=lambda item: item[1], reverse=True)

if __name__ == '__main__':
    filepath = input('Add path to file: ')
    text = load_data(filepath)
    frequent_words = get_most_frequent_words(text)
    i = 0
    for word, count in frequent_words:
        i += 1
        print(word, ' : ', count)
        if i >= 10:
            break

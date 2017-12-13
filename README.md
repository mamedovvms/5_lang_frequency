# Frequency Analysis of Words

The program analyzes the frequency of words in the text


#Procedures

def load_data(filepath) - returns the text of the file

filepath - parameter path to the file with text

def get_most_frequent_words(text) - returns a list of tuples that contain words and the number of their occurrences in the text

text - the text in which the frequency of words is determined


#Example

from lang_freguency import get_most_frequent_words

for word, count in get_most_frequent_words('1.txt')
    print(word, ' - ', count)


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

# Frequency Analysis of Words


The program analyzes the frequency of words in the text and displays 
the most common


#Procedures

```python def load_data(filepath)``` - returns the text of the file
```python def get_most_frequent_words(text)``` - returns a list of tuples of the most popular words that
 contain words and the number of their occurrences in the text, in which the frequency of words is determined


#Example

```bash 

$python lang_frequency.py text.txt -a 3# possibly requires call of python3 executive instead of just python

нет : 1081
type : 1067
publicphone : 1066
```
When launching, the required parameter is set to the path to the file with text,
 and you can set the parameter for how many words to output, by default 10 words will be displayed

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

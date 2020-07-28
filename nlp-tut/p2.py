from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize
import os


stop_words = stopwords.words("english")

# Filtering the data
example_str = "This is just a string to check if nltk is filtering using stop words."

words = word_tokenize(example_str)
print(words)

filtered_words = [w for w in words if not w in stop_words]

print(filtered_words)


# Messing with the text moby dick.

def stop_words_cleaner(text):
    words = word_tokenize(text)
    return [w for w in words if w not in stop_words and w not in punctuation]


with open(os.getcwd() + "/Data/mobydick.txt") as f:
    content = f.read()

moby_dick_filtered = stop_words_cleaner(content)
print(moby_dick_filtered)

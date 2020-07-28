from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os


stop_words = stopwords.words("english")

# Filtering the data
example_str = "This is just a string to check if nltk is filtering using stop words."

words = word_tokenize(example_str)
print(words)

filtered_words = [w for w in words if not w in stop_words]

print(filtered_words)

exit()

# Messing with the text moby dick.

with open(os.getcwd() + "/Data/mobydick.txt") as f:
    content = f.read().split("\n")

# print(stop_words)

clean_data = ""

for line in content:
    clean_data += ' '.join((lambda x: [w for w in x.split() if w not in stop_words])(line))


print(clean_data)


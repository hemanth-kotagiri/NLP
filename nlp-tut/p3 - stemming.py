from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

txt = "Hello, I am a pythoner does pythoning in python considering myself a pythonista as I love pythoning in python."

# Tokenize
words = word_tokenize(txt)

ps = PorterStemmer()
print("Original text: ", txt)
print("After using PorterStemmer:")
for word in words:
    print(ps.stem(word), end=' ')
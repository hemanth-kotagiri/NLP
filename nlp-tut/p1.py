from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello, this is Mr. Hemanth. And this is him messing around with the nltk module. This repo is dedicated to do some cool stuff with nlp!"

print(sent_tokenize(text))
print(word_tokenize(text))

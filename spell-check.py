from textblob import TextBlob


a = "I do not know how to use a computar"
print(f'original text: {a}')
b = TextBlob(a)
print(f'corrected text: {b.correct()}')
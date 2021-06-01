from textblob import TextBlob

misspelt = input("Enter an misspelt sentence")
print(f'original text: {misspelt}')

corrected = TextBlob(misspelt)
print(f'corrected text: {corrected.correct()}')
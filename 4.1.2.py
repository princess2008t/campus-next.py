def translate(sentence):
    words = {
        'esta': 'is',
        'la': 'the',
        'en': 'in',
        'gato': 'cat',
        'casa': 'house',
        'el': 'the'
    }
    translated_words = (words[word] for word in sentence.split())
    return ' '.join(translated_words)

print(translate("el gato esta en la casa"))
def popularity(text):
    words = [word.lower() for word in text.split(' ') if word != '']
    words_dict = {word: words.count(word) for word in set(words)}
    sorted_words_dict = sorted(words_dict.items(), key=lambda item: (-item[1], item[0]))
    return [words for words, _ in sorted_words_dict]

if __name__ == '__main__':
    popularity(input('Enter the text: '))



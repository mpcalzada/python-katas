def spin_words(sentence):
    inverted_sentence = []
    for word in sentence.split(' '):
        inverted_sentence.append(word[::-1] if len(word) > 4 else word)
    return " ".join(inverted_sentence)


if __name__ == '__main__':
    print(spin_words("Welcome to my world"))

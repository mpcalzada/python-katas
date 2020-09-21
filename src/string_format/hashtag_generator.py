def generate_hashtag(s):
    phrase = "".join(map(lambda x: x.capitalize(), s.split()))
    return False if not phrase or len(phrase) > 140 else '#' + phrase


if __name__ == '__main__':
    print(generate_hashtag(''))
    print(generate_hashtag('Codewars'))
    print(generate_hashtag('codewars is nice'))
    print(generate_hashtag('codewars Is Nice'))

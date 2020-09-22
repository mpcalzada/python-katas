def count(string):
    counter = {}
    for c in list(string):
        counter[c] = counter[c] + 1 if c in counter else 1
    return counter


if __name__ == '__main__':
    print(count('aba'))

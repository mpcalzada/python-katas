# Another Solution
# def to_weird_case_word(string):
#    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
# def to_weird_case(string):
#    return " ".join(to_weird_case_word(str) for str in string.split())

def to_weird_case(string):
    up = True
    weir_case = []
    for letter in string:
        if up and letter != ' ':
            letter = letter.upper()
            up = False
        else:
            letter = letter.lower()
            up = True
        weir_case.append(letter)

    return "".join(weir_case)


if __name__ == '__main__':
    print(to_weird_case("Weird string case"))

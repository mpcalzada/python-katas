def to_jaden_case(string):
    # print(" ".join( map( lambda x: x.capitalize() , string.split(' ') ) ))
    return ' '.join([word.capitalize() for word in string.split()])


if __name__ == '__main__':
    quote = "How can mirrors be real if our eyes aren't real"
    print(to_jaden_case(quote))

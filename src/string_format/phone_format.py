def create_phone_number(numbers):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)
    phone_format = '('
    for i in range(len(numbers)):
        if i == 3:
            phone_format = phone_format + ') '
        if i == 6:
            phone_format = phone_format + '-'
        phone_format = phone_format + str(numbers[i])
    return phone_format


if __name__ == '__main__':
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

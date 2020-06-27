def even_or_od(number):
    # return ["Even", "Odd"][number % 2]
    return 'even' if (number % 2 == 0) else 'odd'


if __name__ == '__main__':
    print(even_or_od(1))
    print(even_or_od(2))

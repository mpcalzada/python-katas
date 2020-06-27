def solution(number):
    # return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
    multiples_sum = 0
    for number in range(1, number):
        if number % 3 == 0 or number % 5 == 0:
            multiples_sum += number
    return multiples_sum


if __name__ == '__main__':
    print(solution(10))  # Expected 23
    print(solution(100))  # Expected 2318

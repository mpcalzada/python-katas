def compute_eureka(num, iteration):
    """
    Returns the sum of each digit pow by an incremental iteration
    :rtype: int
    """
    print(f"Iteration: {iteration} for num: {num} compute_num: {str(num)[0:1]} new_num: {str(num)[1::]}")

    if len(str(num)) == 1:
        return int(num) ** iteration

    return int(str(num)[0:1]) ** iteration + compute_eureka(str(num)[1::], iteration + 1)


def sum_digit_pow(a, b):
    """
    Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
    Ej.
    sum_digit_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum_digit_pow(1, 100) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
    :rtype: list
    """
    eurekas = []
    for i in range(a, b + 1):
        calc = compute_eureka(i, 1)
        print(f"Evaluating {calc} vs {i}")
        if calc == i:
            eurekas.append(i)
    return eurekas


if __name__ == '__main__':
    # print(sum_digit_pow(90, 100))
    print(sum_digit_pow(446, 1397))

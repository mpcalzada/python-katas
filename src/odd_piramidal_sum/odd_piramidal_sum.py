def simple_compute_line(expected_line):
    return expected_line * expected_line * expected_line


def complex_compute_line(expected_line):
    value = 1
    values = {0: 1}
    for line in range(1, expected_line):
        count = 0
        sum = 0
        while count <= line:
            value += 2
            count += 1
            sum += value
            print(f"--- Counting [{count}] Value[{value}]")

        values[line] = sum
        print(f"Count [{count}] Value[{value}] Values[{values}]")
    return value


if __name__ == '__main__':
    n = int(input("Ingresa el valor de la linea que deseas"))

    result_by_complex = complex_compute_line(n)
    result_by_simple = simple_compute_line(n)

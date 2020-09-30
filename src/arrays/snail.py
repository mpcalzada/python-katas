def snail(snail_map):
    return []


if __name__ == '__main__':
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    snail_result = snail(array)
    assert snail_result == expected, f'Received: {snail(array)} Expected: {expected} '

    array = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    snail_result = snail(array)
    assert snail_result == expected, f'Received: {snail(array)} Expected: {expected} '

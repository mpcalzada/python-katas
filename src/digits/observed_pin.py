# Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him
# to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an
# electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.
#
# The keypad has the following layout:
#
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
# │ 0 │
# └───┘
# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another
# adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4.
# And instead of the 5 it could also be the 2, 4, 6 or 8.
#
# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally
# lock the system or sound the alarm. That's why we can try out all possible (*) variations.
#
# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits
#
# Can you help us to find all those variations? It would be nice to have a function, that returns an array
# (or a list in Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits.
# We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs,
# the observed one and also the results, must be strings, because of potentially leading '0's.
#
# Detective, we are counting on you!

# BEST SOLUTIONS
# SOLUTION # 1:
# from itertools import product
#
# ADJACENT = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')
#
# def get_pins(observed):
#     return [''.join(p) for p in product(*(ADJACENT[int(d)] for d in observed))]
#
# SOLUTION #2:
# def get_pins(observed):
# map = [['8','0'], ['1','2','4'], ['1','2','3','5'], ['2','3','6'], ['1','4','5','7'], ['2','4','5','6','8'],
#        ['3','5','6','9'], ['4','7','8'], ['5','7','8','9','0'], ['6','8','9']]
# return map[int(observed[0])] if len(observed) == 1 else [x + y for x in map[int(observed[0])] ...
# ... for y in get_pins(observed[1:])]


def get_pins(observed):
    all_possibilities = []
    combinations = []
    for digit_pos in range(0, len(observed)):
        digit = int(observed[digit_pos:digit_pos + 1])
        all_possibilities.append(get_possibilities(digit))
    combine(all_possibilities, '', combinations)
    return combinations


def combine(available_possibilities, current_value, computed_combinations):
    current_len = len(available_possibilities[0])
    is_last = len(available_possibilities) == 1
    for i in range(current_len):
        item = current_value + available_possibilities[0][i]
        if is_last:
            computed_combinations.append(item)
        else:
            combine(available_possibilities[1:], item, computed_combinations)


def get_possibilities(digit):
    possibilities_dic = {
        0: ['0', '8'],
        1: ['1', '2', '4'],
        2: ['1', '2', '3', '5'],
        3: ['2', '3', '6'],
        4: ['1', '4', '5', '7'],
        5: ['2', '4', '5', '6', '8'],
        6: ['3', '5', '6', '9'],
        7: ['4', '7', '8'],
        8: ['5', '7', '8', '9', '0'],
        9: ['6', '8', '9'],
    }
    return possibilities_dic[digit]


if __name__ == '__main__':
    comb = get_pins('100')
    print(f'Final result {comb}')

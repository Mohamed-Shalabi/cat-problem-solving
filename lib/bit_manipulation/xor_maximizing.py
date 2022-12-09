from copy import copy


def maximizing_xor(l, r) -> int:
    numbers = range(l, r + 1)
    numbers_duplication = copy(numbers)
    result: int = -1
    for number in numbers:
        for another_number in numbers_duplication:
            xor = number ^ another_number
            if xor > result:
                result = xor
    return result

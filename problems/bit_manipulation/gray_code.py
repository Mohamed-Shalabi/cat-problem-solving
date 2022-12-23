from functools import reduce


def gray_code(n: int) -> list[int]:
    matrix: list[list[int]] = list(
        [[0]] + [
            [j for j in range(2 ** (i - 1), 2 ** i)]
            for i in range(1, n + 1)
        ]
    )

    matrix.insert(len(matrix), matrix.pop(1))

    for arr in matrix:
        _order_like_triangle(arr)

    return list(reduce(lambda x, y: x + y, matrix))


def _order_like_triangle(arr: list[int]):
    distance = 1
    index = 0
    while index < len(arr) - 1:
        element = arr[index]

        if abs(element.bit_count() - arr[index + 1].bit_count()) != 1:
            arr.insert(len(arr) - distance, arr.pop(index))
            distance += 1
            index -= 2

        if element.bit_count() == len(bin(element).replace('0b', '')):
            break

        index += 1

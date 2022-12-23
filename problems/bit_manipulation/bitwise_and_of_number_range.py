def range_bitwise_and(left: int, right: int) -> int:
    if right == left:
        return right

    bin_right = bin(right)[2:]
    bin_left = bin(left)[2:]
    if len(bin_right) > len(bin_left):
        bin_left = '0' * (len(bin_right) - len(bin_left)) + bin_left

    start = 0
    for i, c_l in enumerate(bin_left):
        c_r = bin_right[i]
        if c_l != c_r:
            start = i
            break

    return int(bin_right[:start] + '0' * (len(bin_right) - start), 2)


print(range_bitwise_and(5, 7))

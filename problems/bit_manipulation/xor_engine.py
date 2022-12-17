import sys


def xor_engine():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n, q = map(int, sys.stdin.readline().strip().split())
        numbers = list(map(int, sys.stdin.readline().strip().split()))
        numbers_even_ones_count, numbers_odd_ones_count = 0, 0

        for number in numbers:
            if bin(number).count('1') % 2 == 0:
                numbers_even_ones_count += 1

        numbers_odd_ones_count = n - numbers_even_ones_count

        for ___ in range(q):
            p = int(sys.stdin.readline().strip())
            if numbers_odd_ones_count == numbers_even_ones_count:
                sys.stdout.write(f'{numbers_even_ones_count} {numbers_odd_ones_count}\n')
                continue

            are_p_ones_even = bin(p).count('1') % 2 == 0
            if are_p_ones_even:
                sys.stdout.write(f'{numbers_even_ones_count} {numbers_odd_ones_count}\n')
            else:
                sys.stdout.write(f'{numbers_odd_ones_count} {numbers_even_ones_count}\n')


xor_engine()

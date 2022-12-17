from functools import reduce
from sys import stdin, stdout


def max_and():
    t = int(read())
    for _ in range(t):
        n = int(read())
        a_list = list(map(int, read().split()))
        a_list.sort(reverse=True)
        b_list = list(map(int, read().split()))
        b_list.sort(reverse=True)
        write(
            reduce(
                lambda c1, c2: c1 & c2, [
                    a & b
                    for (a, b) in
                    [
                        (a_list[i], (b_list[i])) for i in range(n)
                    ]
                ]
            )
        )


def read() -> str:
    return stdin.readline().strip()


def write(i):
    return stdout.write(str(i) + '\n')


max_and()

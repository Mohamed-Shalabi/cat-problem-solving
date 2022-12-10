def xor_engine():
    t = int(input())
    for i in range(t):
        n_q = input().split(' ')
        q = int(n_q[1])
        string_numbers = input().split(' ')
        numbers = map(lambda element: int(element), string_numbers)
        for j in range(q):
            xor_even_ones_results = []
            xor_odd_ones_results = []
            p = int(input())
            for k in numbers:
                xor_result = p ^ k
                binary_xor_result = bin(xor_result).replace('0b', '')
                if binary_xor_result.count('1') % 2 == 0:
                    xor_even_ones_results.append(xor_result)
                if binary_xor_result.count('1') % 2 == 1:
                    xor_odd_ones_results.append(xor_result)
            print(len(xor_even_ones_results), len(xor_odd_ones_results))

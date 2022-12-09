def is_first_element_a_duplication(sorted_list: list[int]) -> bool:
    if len(sorted_list) < 2:
        return False
    first_element = sorted_list[0]
    second_element = sorted_list[1]
    return first_element == second_element


def lonely_integer(a: list) -> int:
    a.sort()
    if is_first_element_a_duplication(a):
        a.pop(0)
        a.pop(0)
        return lonely_integer(a)
    else:
        return a[0]

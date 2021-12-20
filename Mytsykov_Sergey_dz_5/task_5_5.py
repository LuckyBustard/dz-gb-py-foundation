SRC = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def non_repeating_numbers():
    """Возвращает не повторяющиеся цифры в порядке следования в списке"""
    numbers = set()
    repeating = set()
    for el in SRC:
        if el in numbers:
            numbers.discard(el)
            repeating.add(el)
        elif el not in repeating:
            numbers.add(el)
    for key in SRC:
        if key in numbers:
            yield key


print(*non_repeating_numbers())

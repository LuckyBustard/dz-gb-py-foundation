def odd_nums(max):
    """
    :argument max: максимальное число
    Генератор нечетных чисел до максимума
    """
    for i in range(1, max, 2):
        yield i


gen = odd_nums(13)
print('First iterator run')
print(*gen)
print('Second iterator run')
print(*gen)

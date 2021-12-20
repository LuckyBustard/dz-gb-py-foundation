def odd_nums(max):
    """
    :argument max: максимальное число
    Генератор нечетных чисел до максимума
    """
    return (i for i in range(1, max, 2))


gen = (i for i in range(1, 13, 2))
print('First iterator run')
try:
    while True:
        print(next(gen))
except StopIteration:
    print('Stop Iteration')

print('Second iterator run')
print(*gen)
print('Restart iterator')
gen = odd_nums(13)
print(*gen)

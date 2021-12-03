template = 'процент'

for percent in range(1, 101):
    suffix = ''
    modulo = percent % 10
    if 10 <= percent <= 20 or 5 <= modulo <= 9 or modulo == 0:
        suffix = 'ов'
    elif 2 <= modulo <= 4:
        suffix = 'а'
    print(percent, template + suffix)
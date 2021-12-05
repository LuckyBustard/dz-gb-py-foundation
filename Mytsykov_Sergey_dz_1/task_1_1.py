durations = []

duration = 1
while duration != 0:
    duration = int(input('Введите список продолжительностей, 0 закончить ввод: '))
    if duration != 0:
        durations.append(duration)

periods = (86400, 3600, 60)
terms = (' дней ', ' часов ', ' минут')

for duration in durations:
    text_duration = ''

    for period_i in range(len(periods)):
        result = duration // periods[period_i]
        text_duration += str(result) + terms[period_i]

        if result != 0:
            duration %= periods[period_i]

    print(text_duration, duration, 'сек')


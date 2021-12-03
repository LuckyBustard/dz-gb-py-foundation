durations = []

duration = 1
while duration != 0:
    duration = int(input('Введите список продолжительностей, 0 закончить ввод: '))
    if duration != 0:
        durations.append(duration)

for duration in durations:
    if duration < 60:
        print(duration, ':', duration, 'сек')
    elif duration < 3600:
        sec = duration
        min = sec // 60
        sec -= min * 60
        print(duration, ':', min, 'мин', sec, 'сек')
    elif duration < 86400:
        sec = duration
        hour = sec // 3600
        sec -= hour * 3600
        min = sec // 60
        sec -= min * 60
        print(duration, ':', hour, 'час', min, 'мин', sec, 'сек')
    else:
        sec = duration
        day = sec // 86400
        sec -= day * 86400
        hour = sec // 3600
        sec -= hour * 3600
        min = sec // 60
        sec -= min * 60
        print(duration, ':', day, 'дней', hour, 'час', min, 'мин', sec, 'сек')

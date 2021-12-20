TUTORS = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', ]
KLASSES = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', ]


def klasses_asigner():
    """Возвращает картеж из ученика и его класса"""
    for i in range(len(TUTORS)):
        yield TUTORS[i], KLASSES[i] if i < len(KLASSES) else None


klasses = klasses_asigner()
print('Iterator first run')
try:
    while True:
        print(next(klasses))
except StopIteration:
    print('Iterator first stopped')

print('Iterator second run')
try:
    while True:
        print(next(klasses))
except StopIteration:
    print('Iterator second stopped')

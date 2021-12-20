SRC = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def get_greater_numbers():
    previous = 0
    for i in range(len(SRC)):
        if i != 0 and SRC[i] > previous:
            yield SRC[i]
        previous = SRC[i]


print([*get_greater_numbers()])

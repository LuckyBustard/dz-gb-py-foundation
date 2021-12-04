cube_odd_list = []

for i in range(1, 1001):
    if i % 2 == 1:
        cube_odd_list.append(i ** 3)

terms = [0, 17]
for term in terms:
    full_sum = 0

    for i in range(len(cube_odd_list)):
        number = cube_odd_list[i] + term
        digit_sum = 0
        while number > 0:
            digit_sum += number % 10
            number //= 10
        if digit_sum % 7 == 0:
            full_sum += cube_odd_list[i] + term

    print('term:', term, 'sum:' , full_sum)


cube_odd_list = []

for i in range(1, 1001):
    if i % 2 == 1:
        cube_odd_list.append(i ** 3)

full_sum = [0, 0]
term = 17
for i in range(len(cube_odd_list)):
    number = cube_odd_list[i]
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    if digit_sum % 7 == 0:
        full_sum[0] += cube_odd_list[i]
    digit_sum = 0
    number = cube_odd_list[i] + term
    while number > 0:
        digit_sum += number % 10
        number //= 10
    if digit_sum % 7 == 0:
        full_sum[1] += cube_odd_list[i] + term

print(full_sum)

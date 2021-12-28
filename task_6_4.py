with open('data/users.csv', 'r', encoding='utf-8') as users, \
        open('data/hobby.csv', 'r', encoding='utf-8') as hobbyes, \
        open('data/users_hobby.txt', 'w', encoding='utf-8') as users_hobby:
    for user in users:
        hobby = hobbyes.readline().strip()
        if not hobby:
            hobby = None
        users_hobby.write(f"{user.strip()}: {hobby}\n")

    hobby = hobbyes.readline().strip()
    if hobby:
        exit(1)

with open('data/users_hobby.txt', 'r', encoding='utf-8') as users_hobby:
    for user_hobby in users_hobby:
        print(user_hobby.strip())

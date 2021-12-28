from sys import argv

LINE_SIZE = 27

with open('../data/bakery.csv', 'a', encoding='utf-8') as bakery:
    if (int(argv[1]) * LINE_SIZE) > bakery.tell():
        exit(1)

with open('../data/bakery.csv', 'r+', encoding='utf-8') as bakery:
    position = (int(argv[1]) * LINE_SIZE)
    print(bakery.tell())
    bakery.seek(position - LINE_SIZE)
    print(bakery.tell())
    bakery.write(f"{argv[1]:>4}, {argv[2]:>20}\n")

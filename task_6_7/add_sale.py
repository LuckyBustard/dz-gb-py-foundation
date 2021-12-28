from sys import argv

LINE_SIZE = 27

with open('../data/bakery.csv', 'a', encoding='utf-8') as bakery:
    print(bakery.tell())
    uid = int(round(bakery.tell() / LINE_SIZE, 0)) + 1
    bakery.write(f"{uid:>4}, {argv[1]:>20}\n")

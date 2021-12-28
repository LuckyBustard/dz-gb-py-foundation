from sys import argv

LINE_SIZE = 27

with open('../data/bakery.csv', 'r', encoding='utf-8') as bakery:
    if len(argv) == 1:
        for sale in bakery:
            print(sale.strip())
    if len(argv) == 2:
        bakery.seek((int(argv[1]) - 1) * LINE_SIZE)
        for sale in bakery:
            print(sale.strip())
    if len(argv) == 3:
        bakery.seek((int(argv[1]) - 1) * LINE_SIZE)
        while True:
            sale = bakery.readline()
            if sale == '':
                break
            print(sale.strip())
            if bakery.tell() > ((int(argv[2]) - 1) * LINE_SIZE):
                break

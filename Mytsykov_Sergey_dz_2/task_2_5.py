def PrintPrices(prices):
    str_prices = ''
    for price in prices:
        price = str(price).split('.')
        if len(price) == 1:
            price.append('0')
        str_prices += f"{int(price[0])} руб. {int(price[1]):02d} коп; "
    return str_prices


asc_prices = [115.2, 12.23, 57.8, 46.51, 97, 12, 789.1, 42.42, 112.12, 104.03]
asc_prices.sort()
print(PrintPrices(asc_prices))
desc_prices = list(reversed(asc_prices))
print(PrintPrices(desc_prices))
print(PrintPrices(desc_prices[:5]))

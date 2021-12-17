from requests import get
from decimal import Decimal

SERVER_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

response = get(SERVER_URL)


def currency_rates(char_code):
    char_code = char_code.upper()
    response_list = response.text.split('<Valute ID=')
    for response_str in response_list:
        if char_code in response_str:
            start = response_str.find('<Value>') + 7
            end = response_str.find('</Value>')
            return Decimal(response_str[start:end].replace(',', '.'))
    return None


if __name__ == '__main__':
    print(currency_rates('USD'))
    print(currency_rates('EUR'))


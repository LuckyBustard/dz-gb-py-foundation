from requests import get
from decimal import Decimal
from datetime import datetime

SERVER_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(code):
    response = get(SERVER_URL)
    char_code = code.upper()
    answer = {}
    # rate_date = re.search("Date=\"([\d.:]*)\"", response.text).group(1)
    # rate_value = re.search(f"<CharCode>{char_code}[<>\s\w/]+<Value>([\d,]+)", response.text).group(1)
    response_list = response.text.split('<Valute ID=')
    start = response_list[0].find('Date="') + 6
    end = response_list[0].find('" name')
    answer['date'] = datetime.strptime(response_list[0][start:end], '%d.%m.%Y').date()
    for currency_str in response_list:
        if char_code in currency_str:
            start = currency_str.find('<Value>') + 7
            end = currency_str.find('</Value>')
            answer['rate'] = Decimal(currency_str[start:end].replace(',', '.'))
            return answer
    return None


print(currency_rates('USD'))
print(currency_rates('EUR'))

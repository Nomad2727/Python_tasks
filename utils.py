import requests
from decimal import *


def currency_rates(currency):
    find_object = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if currency not in find_object:
        return None

    find_rub = find_object[find_object.find('<Value>', find_object.find(currency)) + 7:find_object.find('</Value>',
                           find_object.find(currency))]

    return Decimal(find_rub.replace(',', '.'))


#print(currency_rates('USD'))

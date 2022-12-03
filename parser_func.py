import datetime
import requests 
from bs4 import BeautifulSoup
from bs4.element import Tag

from price import Price

def get_day_tables(bs4:BeautifulSoup):
    return bs4.select('div table')

def get_prices_from_table(table:Tag):
    date = get_date_for_table(table)
    prices = []
    rows = table.select('tr:has(td.price)')
    for row in rows:
        price = Price()
        price.parse_from_table_row(row, date)
        prices.append(price)

    return prices

def get_date_for_table(table:Tag):
    for previous in table.previous_elements:
        if str(previous).endswith("12.2022"):
            return previous

    return None

def get_parser(data:bytes):
    return BeautifulSoup(data, 'html.parser')

def get_data_from_url(url):
    requests.get(url).content

def get_all_prices_for_tables(tables):
    all_day_prices = []
    for table in tables:        
        all_day_prices.append(get_prices_from_table(table))

    return all_day_prices

def get_all_prices_for_date(given_date:datetime, prices:list):
    flat_list = [item for sublist in prices for item in sublist]
    prices_for_date = []
    for price in flat_list:
        if price.date.date() == given_date.date():
            prices_for_date.append(price)

    return prices_for_date


def intersection(lst1, lst2): 
    return [item for item in lst1 if item in lst2]
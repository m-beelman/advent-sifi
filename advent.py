import os
import requests 
from datetime import datetime
from parser_func import get_all_prices_for_date, get_all_prices_for_tables, get_day_tables, get_parser


numbers_to_check = [423,597,446,566]

def out(str_to_print:str):
    print(str_to_print)

URL = 'https://www.dksb-bb.de/adventskalender2022/'

website = requests.get(URL)
parser = get_parser(website.content)
day_tables = get_day_tables(parser)
all_prices = get_all_prices_for_tables(day_tables)
all_prices_today = get_all_prices_for_date(datetime.now(), all_prices)

date_string = datetime.now().date().strftime("%d.%m.%Y")

out("# Report for " + date_string)
out('|Sponsor    |Price      |Number that wins|Our numbers|')
out('|-----------|-----------|----------------|-----------|')

win = False
for price in all_prices_today:
    win = len(price.check_winner(numbers_to_check)) > 0
    out(f'|{price.sponsor}|{price.price_detail}|{price.winners}|{",".join(price.check_winner(numbers_to_check))}|')

issue_title = f'Report for {date_string}'

if win == True:
    issue_title = f"YOU'VE WON!!! - Report for {date_string}"



with open("xenv.sh", "a") as myfile:
    myfile.write(f'GH_ISSUE_TITLE="{issue_title}"')
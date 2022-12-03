import datetime
from bs4.element import Tag

class Price:
    def __init__(self):
        self.sponsor = ''
        self.price_detail = ''
        self.winners = []
        self.date = None

    def parse_from_table_row(self, table_row:Tag, date:str):
        values = table_row.select('td.price')
        self.sponsor = values[0].text
        self.price_detail = values[1].text
        self.winners = values[2].text
        date_to_parse = date.split(',')[1].strip()
        self.date = datetime.datetime.strptime(date_to_parse, '%d.%m.%Y')

    def check_winner(self, cal_numbers:list):
        our_winners = []
        winner_numbers = [int(numeric_string) for numeric_string in self.winners.split(',')]
        for cal_number in cal_numbers:
            if cal_number in winner_numbers:
                our_winners.append(cal_number)

        return our_winners

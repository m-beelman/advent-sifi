from parser_func import get_day_tables, get_parser, get_prices_from_table

html_test_data = None

def mock_data():
    global html_test_data
    if html_test_data is None:
        with open("test_page.html", "rb", ) as html_file:
            html_test_data = html_file.read()

    return html_test_data

def test_get_parser():    
    parser = get_parser(mock_data())   
    assert(parser != None)

def test_get_day_tables():
    parser = get_parser(mock_data())
    day_tables = get_day_tables(parser)
    assert (len(day_tables)> 3)

def test_get_prices_from_table():
    parser = get_parser(mock_data())
    day_tables = get_day_tables(parser)
    day_prices = []
    for table in day_tables:
        day_prices.append(get_prices_from_table(table))

def test_check_for_winner():
    parser = get_parser(mock_data())
    day_tables = get_day_tables(parser)
    all_day_prices = []
    for table in day_tables:        
        all_day_prices.append(get_prices_from_table(table))
    
    for day_prices in all_day_prices:
        for day_price in day_prices:            
            assert(len(day_price.check_winner([423,597,446,566])) == 0)

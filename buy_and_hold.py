import csv
from datetime import date

def get_price(stock, date):
    with open(stock, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Date'] == date:
                return float(row['Price'])

        return None

def validate_dates(date_buy, date_sell):
    try:
        b_year, b_month, b_day = date_buy.split('-')
        s_year, s_month, s_day = date_sell.split('-')
        difference = date(int(s_year), int(s_month), int(s_day)) - date(int(b_year), int(b_month), int(b_day))
        if difference.days <= 0:
            return False
        else:
            return True
    except ValueError:
        return False

def calculate_return_1(stock, date_buy, date_sell):
    if not validate_dates(date_buy, date_sell):
        return "Invalid Dates. You cannot sell a stock before you buy it."

    price_buy = get_price(stock, date_buy)
    price_sell = get_price(stock, date_sell)

    if price_buy is None or price_sell is None:
        return "Invalid Dates. The stock market may not have been open on one of these days, please try again."

    absolute_return = price_sell - price_buy
    return round((absolute_return/price_buy)*100, 2)

def buy_and_hold(stock):
    purchase_price, sell_price = get_price_first_last(stock)
    return calculate_return(purchase_price, sell_price)

def calculate_return(price_1, price_2):
    absolute_return = price_2 - price_1
    return round((absolute_return/price_1)*100, 2)

def get_price_first_last(stock):
    with open(stock, "r") as file:
        reader = csv.DictReader(file)
        first_price = float(next(reader)["Price"])
        for row in reader:
            last_price = float(row['Price'])
        return (first_price, last_price)



def main():
    print(buy_and_hold("AAPL_2024.csv"))

if __name__ == __main__:
    main()

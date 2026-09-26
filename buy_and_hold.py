import csv
from datetime import date

#return price of stock for a given date for foundational function
def get_price(stock, date):
    with open(stock, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['Date'] == date:
                return float(row['Price'])

        return None

#verify validity of buy and sell dates within a given year of market prices
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

#creating a simple "buy and hold" function
def buy_and_hold(stock):
    purchase_price, sell_price = get_price_first_last(stock)
    return calculate_return(purchase_price, sell_price)

#calculate the absolute return given two prices
def calculate_return(price_1, price_2):
    absolute_return = price_2 - price_1
    return round((absolute_return/price_1)*100, 2)

#a more specific function that returns the price of the stock on the first and last day of market
def get_price_first_last(stock):
    with open(stock, "r") as file:
        reader = csv.DictReader(file)
        first_price = float(next(reader)["Price"])
        for row in reader:
            last_price = float(row['Price'])
        return (first_price, last_price)
        
#incorporate shares and available cash to create a buy and sell function
def buy_action(cash, number_shares, share_price):
    if share_price <= cash:
        cash -= share_price
        number_shares += 1
    return (cash, number_shares)

def sell_action(cash, number_shares, share_price):
    if number_shares > 0:
        cash += share_price
        number_shares -= 1
    return (cash, number_shares)

#create a function that creates a buy signal if the price increases compared to the day before, sells if it decreases and holds if its the same
def buy_or_sell_signal(stock):


def main():
    print(buy_and_hold("AAPL_2024.csv"))

if __name__ == "__main__":
    main()

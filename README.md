# Stock Price Backtester

A beginner Python project for testing simple trading strategies against historical stock-price data.

This project was created as my final project for Harvard's CS50P course. I am using it to learn the fundamentals of Python programming and explore how quantitative trading strategies can be implemented and evaluated.

## Current Features

- Read historical stock-price data from CSV files
- Retrieve the price of a stock on a specific date
- Validate trading dates
- Calculate percentage returns between two prices
- Calculate the return of a simple buy-and-hold strategy
- Track cash and shares when executing individual buy and sell actions
- Develop a simple price-movement trading strategy

## How It Works

The project is built from several small functions:

- `get_price()` retrieves the price for a given stock and date.
- `validate_dates()` checks whether a pair of trading dates is valid.
- `calculate_return()` calculates the percentage return between two prices.
- `get_price_first_last()` retrieves the first and last prices in a dataset.
- `buy_and_hold()` calculates the return from buying at the beginning of the dataset and selling at the end.
- `buy_action()` and `sell_action()` update the portfolio's cash and number of shares when a trade is executed.

The current trading strategy compares each day's price with the previous day's price:

- Price increases → BUY
- Price decreases → SELL
- Price stays the same → HOLD

## Data

The project currently uses historical stock-price data stored in CSV files.

## Future Development

I plan to continue developing the backtester by adding:

- Portfolio simulation over multiple trading days
- Performance comparison between different strategies
- Additional trading strategies
- Support for multiple stocks
- Portfolio performance metrics
- Potentially retrieving data through an API rather than CSV files

## Disclaimer

This project is for educational purposes only and is not intended to provide financial advice or investment recommendations.

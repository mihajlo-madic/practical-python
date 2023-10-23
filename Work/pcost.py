# pcost.py
#
# Exercise 1.27

import csv
from pprint import pprint


def portfolio_cost(filename: str):
    """Computes total cost contained in a given portfolio"""
    total_cost = 0
    portfolio = []
    with open(filename, "rt") as portfolio_file:
        rows = csv.reader(portfolio_file)
        headers = next(rows)
        for i, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                shares = int(record["shares"])
                price = float(record["price"])
                portfolio.append(record)
            except ValueError:
                print(f"Error in line {i}; couldn't parse {row}")
    return portfolio


portfolio = portfolio_cost("Data/portfoliodate.csv")

total_cost = sum([int(stock["shares"]) * float(stock["price"]) for stock in portfolio])

pprint(portfolio)
print(f"Total cost: {total_cost}")

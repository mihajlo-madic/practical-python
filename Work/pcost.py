#! /usr/bin/python3
# pcost.py
#
# Exercise 1.27

import csv
from pprint import pprint
from stock import Stock


def read_portfolio(lines: str):
    """Computes total cost contained in a given portfolio"""
    portfolio = []
    rows = csv.reader(lines)
    headers = next(rows)
    for i, row in enumerate(rows):
        record = dict(zip(headers, row))
        try:
            record["shares"] = int(record["shares"])
            record["price"] = float(record["price"])
            portfolio.append(record)
        except ValueError:
            print(f"Error in line {i}; couldn't parse {row}")
    return portfolio


with open("Data/portfolio.csv", "rt") as csv_file:
    portfolio = [Stock(**stock) for stock in read_portfolio(csv_file)]

pprint(portfolio)
total_cost = sum([stock.price * stock.shares for stock in portfolio])

stock0 = portfolio[0]

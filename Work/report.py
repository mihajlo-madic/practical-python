# report.py
#
# Exercise 2.4

import csv
from pprint import pprint
import pcost


def calculate_prices(filename: str):
    with open(filename, "rt") as prices_file:
        rows = csv.reader(prices_file)
        prices = {}
        for row in rows:
            if row == []:
                continue
            key, value = row
            prices[key] = float(value)
    return prices


portfolio = pcost.portfolio_cost("Data/portfoliodate.csv")
prices = calculate_prices("Data/prices.csv")

pprint(prices)
pprint(portfolio)

priceslist = dict(zip(prices.values(), prices.keys()))

print(min(priceslist))
print(max(priceslist))
print(sorted(priceslist))

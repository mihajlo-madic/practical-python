import csv
from pprint import pprint

with open("Data/portfolio.csv", "rt") as portfolio_csv:
    rows = csv.reader(portfolio_csv)
    headers = next(rows)
    types = [str, int, float]
    portfolio = [dict(zip(headers, row)) for row in rows]

pprint(portfolio)

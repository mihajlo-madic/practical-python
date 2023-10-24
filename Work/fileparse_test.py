#! /usr/bin/python3

import fileparse
from pprint import pprint


if __name__ == "__main__":
    with open("Data/portfoliodate.csv", "rt") as csv_file:
        portfolio_date = fileparse.parse_csv(
            csv_file,
            has_headers=True,
            select=["name", "date", "price"],
            types=[str, str, float],
        )
        pprint(portfolio_date)

    with open("Data/portfolio.dat", "rt") as csv_file:
        portfolio = fileparse.parse_csv(
            csv_file,
            delimiter=" ",
            types=[str, int, float],
            has_headers=True,
        )
        pprint(portfolio)

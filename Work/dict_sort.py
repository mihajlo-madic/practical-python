from pprint import pprint

dicts = [
    {"name": "AA", "price": 32.2, "shares": 100},
    {"name": "IBM", "price": 91.1, "shares": 50},
    {"name": "CAT", "price": 83.44, "shares": 150},
    {"name": "MSFT", "price": 51.23, "shares": 200},
    {"name": "GE", "price": 40.37, "shares": 95},
    {"name": "MSFT", "price": 65.1, "shares": 50},
    {"name": "IBM", "price": 70.44, "shares": 100},
]

pprint(dicts)

dicts.sort(key=lambda stock: stock["name"])

pprint(dicts)

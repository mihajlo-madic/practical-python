# fileparse.py
#
# Exercise 3.3

import csv
from pprint import pprint


def parse_csv(
    lines,
    select: list = None,
    types: list = None,
    has_headers: bool = False,
    delimiter: str = ",",
) -> list:
    """Parses CSV files of arbitrary formats

    Returns:
        list: list of dictionaries if headers are provided, or list
        of tuples if not
    """
    if types and select and len(types) != len(select):
        raise ValueError("Length of types and select arrays must be same!")
    rows = csv.reader(lines, delimiter=delimiter)
    headers = []
    if has_headers:
        headers = next(rows)
    selected_indices = []
    if headers and select:
        selected_indices = [headers.index(colname) for colname in select]
        headers = select
    table = []
    # delimiter functionality
    for row in rows:
        if not row:
            continue
        # select functionality
        if selected_indices:
            row = [cell for i, cell in enumerate(row) if i in selected_indices]
        # type conversion functionality
        if types:
            row = [_type(cell) for _type, cell in zip(types, row)]
        if headers:
            table.append(dict(zip(headers, row)))
        else:
            table.append(tuple(row))
    return table

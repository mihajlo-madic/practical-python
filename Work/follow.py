# follow.py
import os
import time


# producer
def listen_file_updates(log_file):
    stocks_log_file.seek(0, os.SEEK_END)  # Move file pointer 0 bytes from end of file

    while True:
        new_line = log_file.readline()
        if new_line == "":
            time.sleep(0.1)  # Sleep briefly and retry
            continue
        yield new_line


def make_dict_from_stocks_info(stock_update_generator):
    for stock_info in stock_update_generator:
        fields = stock_info.split(",")
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])

        yield {"name": name, "price": price, "change": change}


def filter_stocks(stock_dict_generator, stock_names):
    for stock_dict in stock_dict_generator:
        if stock_dict["name"] in stock_names:
            yield stock_dict


def format_stocks_info(stocks_dict_generator):
    for stocks_dict in stocks_dict_generator:
        yield f"{stocks_dict['name']:>10s} {stocks_dict['price']:>10.2f} {stocks_dict['change']:>10.2f}"


with open("Data/stocklog.csv") as stocks_log_file:
    file_updates_listener = listen_file_updates(stocks_log_file)
    stock_dictionaries = make_dict_from_stocks_info(file_updates_listener)
    filtered_dictionaries = filter_stocks(stock_dictionaries, ["XOM", "IBM", "MSFT"])
    # final consumer
    for formatted_stock_info in format_stocks_info(filtered_dictionaries):
        print(formatted_stock_info)

import argparse
import json
import sys
import os
import finnhub
import requests
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--symbol",
                    dest="symbol",
                    help="Set stock symbol",
                    action='store')
parser.add_argument("-l", "--lookup",
                    dest="lookup",
                    help="Search for stock symbol",
                    action='store')

args = parser.parse_args()

symbol = args.symbol if args.symbol else None
lookup = args.lookup if args.lookup else None


API_KEY = os.environ['STOCK_API_KEY']


def main(symbol=symbol, lookup=lookup):
    """main.
    :param symbol:
    """
    finnhub_client = finnhub.Client(api_key=API_KEY)
    if not symbol and not lookup:
        print(parser.print_help())
        sys.exit('[!] Please provide a stock symbol. ie: DIS, AAPL\n')

    if symbol:
        symbol = symbol.upper()
        response = finnhub_client.quote(symbol)
        stock_price = f"${response['c']}"
        print(f"{symbol}: {colored(stock_price,'blue')}")
    if lookup:
        response = finnhub_client.symbol_lookup(lookup)
        for stock in response['result']:
            print(f"\nCOMPANY: {stock['description']}")
            print(f"SYMBOL: {stock['symbol']}\n")
        print(f"\n[.] Total Results: {response['count']}")


if __name__ == '__main__':
    main(symbol=symbol, lookup=lookup)

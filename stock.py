import argparse
import os
import sys

import finnhub
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
parser.add_argument("-p", "--profile",
                    dest="profile",
                    help="Get company profile",
                    action='store')

args = parser.parse_args()

symbol = args.symbol if args.symbol else None
lookup = args.lookup if args.lookup else None
profile = args.profile if args.profile else None


API_KEY = os.environ['STOCK_API_KEY']


def main(symbol=symbol, lookup=lookup, profile=profile):
    finnhub_client = finnhub.Client(api_key=API_KEY)
    if not symbol and not lookup and not profile:
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
    if profile:
        profile = profile.upper()
        response = finnhub_client.company_profile2(symbol=profile)
        stock_name = f"{response['name']}"
        stock_country = f"{response['country']}"
        stock_exchange = f"{response['exchange']}"
        stock_ipo = f"{response['ipo']}"
        stock_url = f"{response['weburl']}"
        print(f"{colored('*', 'green')}"*25)
        print(f"\t{colored(profile, 'green')}")
        print(f"{colored('*', 'green')}"*25)
        print(f"- Stock Name: {colored(stock_name,'blue')}")
        print(f"- Stock Country: {colored(stock_country,'blue')}")
        print(f"- Stock Exchange: {colored(stock_exchange,'blue')}")
        print(f"- Stock IPO: {colored(stock_ipo,'blue')}")
        print(f"- Stock URL: {colored(stock_url,'blue')}")
        response = finnhub_client.quote(profile)
        stock_price = f"${response['c']}"
        print(f"- Stock Price: {colored(stock_price,'yellow')}")


if __name__ == '__main__':
    main(symbol=symbol, lookup=lookup, profile=profile)

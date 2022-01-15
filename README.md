# stock

quick script that queries for stock prices and looks up stock symbols

## Prequirements:

    Free api key from: https://finnhub.io/ is needed.

## Setup:

    1. sudo pip install -r requirements.txt
    2. export STOCK_API_KEY=<your-finnhub-api-key>

## Usage:

    usage: stock.py [-h] [-l LOOKUP] [-p PROFILE]

## Example Output

```
➜  python3 stock.py -p AAPL
*************************
        AAPL
*************************
- Stock Name: Apple Inc
- Stock Country: US
- Stock Exchange: NASDAQ NMS - GLOBAL MARKET
- Stock IPO: 1980-12-12
- Stock URL: https://www.apple.com/
- Stock Price: $173.07

```

## Optional:

Very useful if a bash alias is created

Modify .bashrc file with something like these Examples:

    alias stock='python3 /<path>/stock.py -s your-symbol'

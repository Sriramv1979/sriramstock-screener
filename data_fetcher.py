import yfinance as yf

def fetch_data(symbol, interval='5m', period='1d'):
    data = yf.download(tickers=symbol, interval=interval, period=period)
    return data

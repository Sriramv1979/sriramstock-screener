import streamlit as st
import pandas as pd
import yfinance as yf
import ta

# Helper functions
def fetch_data(symbol, interval='5m', period='1d'):
    data = yf.download(tickers=symbol, interval=interval, period=period)
    return data

def add_indicators(df):
    df['EMA50'] = ta.trend.ema_indicator(df['Close'], window=50)
    df['RSI'] = ta.momentum.rsi(df['Close'], window=14)
    df['SAR'] = ta.trend.psar(df['High'], df['Low'], df['Close']).psar()
    return df

def is_long_entry(row):
    return row['Close'] > row['EMA50'] and row['RSI'] >= 50 and row['SAR'] < row['Close']

def is_short_entry(row):
    return row['Close'] < row['EMA50'] and row['RSI'] < 50 and row['SAR'] > row['Close']

# Streamlit App
st.title("✅ NSE F&O Momentum Screener")

symbols = ['RELIANCE.NS', 'INFY.NS', 'TCS.NS', 'ICICIBANK.NS', 'HDFCBANK.NS']

long_signals = []
short_signals = []

for symbol in symbols:
    try:
        df = fetch_data(symbol)
        df = add_indicators(df)
        last = df.iloc[-1]
        if is_long_entry(last):
            long_signals.append(symbol)
        elif is_short_entry(last):
            short_signals.append(symbol)
    except Exception as e:
        st.error(f"{symbol} - {e}")

st.subheader("📈 Long Candidates (Top 5)")
st.write(long_signals[:5])

st.subheader("📉 Short Candidates (Top 5)")
st.write(short_signals[:5])

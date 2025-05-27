import streamlit as st
import pandas as pd
from app.data_fetcher import fetch_data
from app.indicators import add_indicators
from app.screener import is_long_entry, is_short_entry

st.title("NSE F&O Momentum Screener")

symbols = ['RELIANCE.NS', 'INFY.NS', 'TCS.NS', 'ICICIBANK.NS', 'HDFCBANK.NS']  # Replace with F&O list

long_candidates = []
short_candidates = []

for symbol in symbols:
    df = fetch_data(symbol)
    df = add_indicators(df)
    latest = df.iloc[-1]
    if is_long_entry(latest):
        long_candidates.append(symbol)
    elif is_short_entry(latest):
        short_candidates.append(symbol)

st.subheader("Top 5 Long Candidates")
st.write(long_candidates[:5])

st.subheader("Top 5 Short Candidates")
st.write(short_candidates[:5])
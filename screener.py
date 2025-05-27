def is_long_entry(row):
    return row['Close'] > row['EMA50'] and row['RSI'] >= 50 and row['SAR'] < row['Close']

def is_short_entry(row):
    return row['Close'] < row['EMA50'] and row['RSI'] < 50 and row['SAR'] > row['Close']

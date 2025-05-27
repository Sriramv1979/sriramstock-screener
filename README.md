# NSE F&O Momentum Screener

This project screens top NSE F&O stocks based on price momentum and applies technical indicators like EMA, RSI, and Parabolic SAR for entry and exit signals.

## Indicators
- 50 EMA
- RSI (middle band 50)
- Parabolic SAR

## Entry Conditions
- Long: Close > EMA50, RSI >= 50, SAR < Close
- Short: Close < EMA50, RSI < 50, SAR > Close
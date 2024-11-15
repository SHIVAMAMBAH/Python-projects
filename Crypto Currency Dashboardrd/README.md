## Crypto Currency Dashboard

The Crypto Currency Dashboard is a web based aapplication that allows users to track and visualize real-time data on various cryptocurrencies. The Dashboard provides insightes into Current prizes, market trends, historical data, and more.



## API Reference

#### Binance API

```http
  https://api.binance.com/api/v3/klines
```

### Query Parameter

#### Sybmols(strings): 
Trading pair symbols (e.g. BTCUSD for Bitcoin to USDT)

#### Interal(string):
Time interval for candlesticks (e.g. 1m, 5m, 1h, 1d).

#### startTime:
Start time in milliseconds to fetch data from.

#### endTime:
End time in milliseconds to fetch data from.

## Usage in the Project
In the Crypto Currency Dashboard, this API is used to retrieve and display hidtorical price data for various crypto Currencies. The data is processed and visualised in the form of candle stick charts. allowing user to analyze market trends over different time periods.


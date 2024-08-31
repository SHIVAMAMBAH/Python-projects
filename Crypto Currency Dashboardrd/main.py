import dash
from dash import dcc, html, Input, Output

import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import pandas_ta as ta

import requests

app = dash.Dash()

app.layout = html.Div([
    dcc.Dropdown(["BTCUSDT", "ETHUSDT", "XRPUSDT"], id="coin-select", value="BTCUSDT"),
    dcc.Dropdown(["1m", "1h", "1d"], id="timeframe-select", value="1m"),
    dcc.Dropdown(["20", "50", "100"], id="num-bars-select", value="20"),
  
    html.Div([
    dcc.RangeSlider(
        min=0, max=100, step=1, value=[0, 20], id="range-slider"
    )],id = "range-slider-container"),
  
    html.H1(id="count-up"),
  
    dcc.Interval(id="interval", interval=2000),
  
    html.Div([
    dcc.Graph(id="candles",style={"border":"2px solid #000","border-radius":"10px","margin":"5px"}),
    ]),
  
    html.Div([
    dcc.Graph(id="indicator",style={"border":"2px solid #000","border-radius":"10px","margin":"5px"}),
    ]),
    
])
@app.callback(
    Output("range-slider-container","children"),
    Input("num-bars-select","value")
)
def update_rangeslider(num_bars):
    return dcc.RangeSlider(min=0, max=int(num_bars), step = int(int(num_bars)/20),value = [0,int(num_bars)],id = "range-slider")

@app.callback(
    [Output("candles", "figure"), Output("indicator", "figure")],
    [Input("interval", "n_intervals"), Input("coin-select", "value")],
    [Input("timeframe-select", "value"), Input("num-bars-select", "value")],
    Input("range-slider", "value")
)
def update_figure(n_intervals, coin_pair, timeframe, num_bars, range_values):
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": coin_pair,
        "interval": timeframe,
        "limit": int(num_bars) + 14  
    }

    data = requests.get(url, params=params).json()
    data = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

    data["rsi"] = ta.rsi(data['close'].astype(float))
    data = data.iloc[14:]  

    start = max(range_values[0], 0)
    end = min(range_values[1], len(data))
    data = data.iloc[start:end]
    
    candles = go.Figure(
        data=[go.Candlestick(
            x=data['timestamp'],
            open=data['open'].astype(float),
            high=data['high'].astype(float),
            low=data['low'].astype(float),
            close=data['close'].astype(float)
        )]
    )
    
    candles.update_layout(xaxis_rangeslider_visible=False, height=600)
    
    indicator = px.line(x=data['timestamp'], y=data['rsi'], height=300)
    
    print(data)
    return candles, indicator

if __name__ == "__main__":
    app.run_server(debug=True)

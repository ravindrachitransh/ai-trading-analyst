import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime


print("Starting...")

stock = yf.Ticker("RELIANCE.NS")

data = stock.history(period="1mo")

print(data.columns)

fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])
fig.show()
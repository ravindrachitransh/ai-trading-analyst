# data.py

import yfinance as yf


def fetch_stock_data(ticker, period="1mo"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def calculate_rsi(data):
    changes = data["Close"].diff()

    gains = changes.clip(lower=0)
    losses = -changes.clip(upper=0)

    avg_gain = gains.mean()
    avg_loss = losses.mean()

    if avg_loss == 0:
        return 100

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    return rsi


def get_stock_metrics(data):

    close_prices = data["Close"].dropna()

    latest_price = close_prices.iloc[-1]

    avg_volume = data["Volume"].mean()

    trend = (
        "upward"
        if latest_price > close_prices.iloc[0]
        else "downward"
    )

    rsi = calculate_rsi(data)

    return {
        "latest_price": round(latest_price, 2),
        "avg_volume": round(avg_volume, 2),
        "trend": trend,
        "rsi": round(rsi, 2),
    }
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from data import calculate_rsi, get_stock_metrics
from ai import generate_report

from fastapi import FastAPI
import yfinance as yf

from data import calculate_rsi

app = FastAPI()

@app.get("/stock/{ticker}")

def get_stock(ticker: str):
    
    stock = yf.Ticker(ticker)
    data = stock.history(period="1mo")
    
    
    metric = get_stock_metrics(data)
    rsi = metric["rsi"]
    report = generate_report(metric, uploaded_file=None)
    
    latest_price = metric["latest_price"]
    trend = metric["trend"]

    return {
        "ticker": ticker,
        "latest price": latest_price,
        "rsi": rsi,
        "avg volume": metric["avg_volume"],
        "trend": trend,
        "report": report
    } 
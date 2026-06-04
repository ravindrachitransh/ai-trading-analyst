import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from data import calculate_rsi, get_stock_metrics, fetch_stock_data
from ai import generate_report

# Debugging: Check where generate_report is being imported from
# print("MODULE:", generate_report.__module__)
# print("FILE:", generate_report.__code__.co_filename)

from fastapi import FastAPI
from fastapi import UploadFile, File, Form
import yfinance as yf



from data import calculate_rsi

app = FastAPI()

# @app.get("/stock/{ticker}")

# def get_stock(ticker: str): 
    
#     stock = yf.Ticker(ticker)
#     data = stock.history(period="1mo")
    
    
#     metric = get_stock_metrics(data)
#     rsi = metric["rsi"]
#     report = generate_report(metric, uploaded_file=None)
    
#     latest_price = metric["latest_price"]
#     trend = metric["trend"]

#     return {
#         "ticker": ticker,
#         "latest price": latest_price,
#         "rsi": rsi,
#         "avg volume": metric["avg_volume"],
#         "trend": trend,
#         "report": report
#     } 
    
    


@app.post("/analyze")
def analyze(
    ticker: str = Form(...),
    uploaded_file: UploadFile = File(None)
): 

    
    data = fetch_stock_data(ticker)
    
    
    metric = get_stock_metrics(data)
    rsi = metric["rsi"]
    
    # Debugging: Print info about the uploaded file
    
    # print("ABOUT TO CALL GENERATE_REPORT")
    # print("uploaded_file =", uploaded_file)
    # print("type =", type(uploaded_file))
    
    report = generate_report(metric, uploaded_file=uploaded_file)
    
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
    
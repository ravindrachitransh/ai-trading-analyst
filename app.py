# app.py

from dotenv import load_dotenv
import os

load_dotenv()

from urllib import request

import streamlit as st
import base64
import requests

from data import fetch_stock_data, get_stock_metrics
from charts import create_candlestick_chart


st.title("📈 AI Trading Analyst")

st.write("Enter a stock symbol (Example: RELIANCE.NS)")

ticker = st.text_input("Stock Symbol")

# Upload an image file with stock data (optional)

uploaded_file = st.file_uploader("Or upload an image file with stock data")

# Debugging: Display uploaded file info

# st.write("Outside button:", uploaded_file)

if uploaded_file is not None:
    

    st.image(uploaded_file, caption="Uploaded Stock Data", width="content")



if st.button("Analyze Stock"):

    try:

        payload = {
            "ticker": ticker
        }

        files = None

        if uploaded_file is not None:
            files = {
                "uploaded_file": (
                    uploaded_file.name,
                    uploaded_file,
                    uploaded_file.type
                )
            }
            
        # Debugging: Display payload and file info before sending request
        # st.write("uploaded_file =", uploaded_file)
        # if uploaded_file is not None:
        #     st.write(uploaded_file.name)

        backend_url = os.getenv("BACKEND_URL")

        response = requests.post(
            f"{backend_url}/analyze",
            data=payload,
            files=files
        )
        
        # st.write(response.status_code)
        # st.write(response.text)
        
        data = response.json()

        print("RESPONSE DATA:", data)
        
        #### Earlier it worked but now data has changed to .json() format, so we need to access the fields accordingly
        
        st.write(data["report"])
        # st.write(f"Latest Price: {data['latest price']}")
        # st.write(f"RSI: {data['rsi']}")
        # st.write(f"Average Volume: {data['avg volume']}")
        # st.write(f"Trend: {data['trend']}")


        ### This repeats the same API call to fetch stock data, but we can optimize it later by including the necessary data in the API response
        
        stock_data = fetch_stock_data(ticker)

        fig = create_candlestick_chart(stock_data)

        st.plotly_chart(fig)
        
        ### this part is for displaying the metrics and report, but we can optimize it by including the necessary data in the API response instead of making another call to fetch stock data

        # # Display metrics
        # column_1, column_2, column_3, column_4 = st.columns(4)

        # with column_1:
        #     st.metric(
        #         "Latest Price",
        #         metrics["latest_price"]
        #     )

        # with column_2:
        #     st.metric(
        #         "Average Volume",
        #         metrics["avg_volume"]
        #     )

        # with column_3:
        #     st.metric(
        #         "Trend",
        #         metrics["trend"].capitalize()
        #     )

        # with column_4:
        #     st.metric(
        #         "RSI",
        #         metrics["rsi"]
        #     )

        # # Display AI report
        # st.subheader("🤖 AI Trading Report")

        # st.write(report)

        # st.success("Analysis completed!")

    except Exception as e:
        st.error(f"Error: {e}")
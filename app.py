# app.py

from urllib import request

import streamlit as st
import base64
import requests

from data import fetch_stock_data, get_stock_metrics
from charts import create_candlestick_chart
from ai import generate_report


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

        response = requests.post(
            "http://localhost:8000/analyze",
            data=payload,
            files=files
        )
        
        # st.write(response.status_code)
        # st.write(response.text)
        
        data = response.json()

        st.write(data["report"])

        st.write(f"Latest Price: {data['latest price']}")
        st.write(f"RSI: {data['rsi']}")
        st.write(f"Average Volume: {data['avg volume']}")
        st.write(f"Trend: {data['trend']}")



        # # Create chart
        # fig = create_candlestick_chart(data)


        # # Display chart
        # st.plotly_chart(fig)

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
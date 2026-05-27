# charts.py

import plotly.graph_objects as go


def create_candlestick_chart(data):

    fig = go.Figure(
        data=[
            go.Candlestick(
                x=data.index,
                open=data["Open"],
                high=data["High"],
                low=data["Low"],
                close=data["Close"]
            )
        ]
    )

    fig.update_layout(
        title="Stock Price Chart",
        xaxis_title="Date",
        yaxis_title="Price"
    )

    return fig
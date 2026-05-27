import yfinance as yf

print("Starting...")

stock = yf.Ticker("TCS.NS")

data = stock.history(period="1mo")

# Closing prices
close_prices = data["Close"]

print("CLOSING PRICES")
print(close_prices)

# Daily price changes
changes = close_prices.diff()

print("\nDAILY CHANGES")
print(changes)

# Gains
gains = changes.clip(lower=0)

# Losses
losses = -changes.clip(upper=0)

print("\nGAINS")
print(gains)

print("\nLOSSES")
print(losses)

# Average gain/loss
avg_gain = gains.mean()
avg_loss = losses.mean()

print("\nAVERAGE GAIN:", avg_gain)
print("AVERAGE LOSS:", avg_loss)

# Relative strength
rs = avg_gain / avg_loss

# RSI formula
rsi = 100 - (100 / (1 + rs))

print("\nRSI:", rsi)
import yfinance as yf

# Ask the user for stock information
ticker = input("Enter the stock ticker: ").upper()
shares = float(input("How many shares did you buy? "))
purchase_price = float(input("What price did you buy each share for? "))

# Get stock data
stock = yf.Ticker(ticker)
history = stock.history(period="1mo")

# Get the most recent closing price
current_price = history["Close"].iloc[-1]

# Calculate values
amount_invested = shares * purchase_price
current_value = shares * current_price
gain_loss = current_value - amount_invested

# Display results
print("\n--- Stock Summary ---")
print("Stock:", ticker)
print("Shares owned:", shares)
print("Purchase price: $", round(purchase_price, 2))
print("Current price: $", round(current_price, 2))
print("Amount invested: $", round(amount_invested, 2))
print("Current value: $", round(current_value, 2))
print("Gain/Loss: $", round(gain_loss, 2))
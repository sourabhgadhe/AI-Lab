import random

# Define a function to generate a random stock price between $10 and $100
def get_stock_price():
    return round(random.uniform(10.0, 100.0), 2)

# Define a function to recommend a trade based on the current stock price
def recommend_trade(price):
    if price < 50:
        return "Buy"
    elif price >= 50 and price < 80:
        return "Hold"
    else:
        return "Sell"

# Define the main function that simulates a trading day
def main():
    # Get the current stock price
    stock_price = get_stock_price()
    # Print the current stock price
    print(f"The current stock price is ${stock_price}")
    # Get a trade recommendation based on the current stock price
    trade_recommendation = recommend_trade(stock_price)
    # Print the trade recommendation
    print(f"We recommend you {trade_recommendation} the stock.")

# Call the main function
main()

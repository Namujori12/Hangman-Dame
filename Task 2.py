# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Number of different stocks
n = int(input("Enter number of stocks you want to buy: "))

for i in range(n):
    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("Stock Price:", stock_prices[stock])
        print("Investment:", investment)

    else:
        print("Stock not available.")

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment: ₹", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")
    file.write("Total Investment: ₹" + str(total_investment))

print("Result saved in portfolio.txt")4

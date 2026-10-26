
# Stock Portfolio Tracker

# Store predefined stock prices
stock_prices = {
    "AAPL": 230,
    "TSLA": 250,
    "GOOGL": 180,
    "MSFT": 420,
    "AMZN": 200
}

portfolio = []
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: Rs. {price}")

while True:
    stock_name = input(
        "\nEnter stock symbol (or 'done' to finish): "
    ).upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock symbol. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity

    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    total_investment += investment

    print(f"Investment in {stock_name}: Rs. {investment}")

print("\n===== Portfolio Summary =====")

if portfolio:
    for item in portfolio:
        print(
            f"{item['stock']} | "
            f"Quantity: {item['quantity']} | "
            f"Price: Rs. {item['price']} | "
            f"Investment: Rs. {item['investment']}"
        )

    print(f"\nTotal Investment: Rs. {total_investment}")

    save_file = input(
        "Do you want to save the portfolio? (yes/no): "
    ).lower().strip()

    if save_file == "yes":
        with open("portfolio.txt", "w", encoding="utf-8") as file:
            file.write("Stock Portfolio Summary\n")

            for item in portfolio:
                file.write(
                    f"{item['stock']}, "
                    f"Quantity: {item['quantity']}, "
                    f"Price: Rs. {item['price']}, "
                    f"Investment: Rs. {item['investment']}\n"
                )

            file.write(
                f"\nTotal Investment: Rs. {total_investment}\n"
            )

        print("Portfolio saved to portfolio.txt")
else:
    print("No stocks were added to the portfolio.")

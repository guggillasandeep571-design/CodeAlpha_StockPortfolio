# Stock Portfolio Tracker Using Python

## Description
A simple Python application that allows users to enter stock names and quantities, calculates the total investment using predefined stock prices, and optionally saves the portfolio details to a text file.

## Features
- Displays predefined stock prices.
- Accepts stock names and quantities from the user.
- Calculates the investment value for each stock.
- Calculates the total portfolio investment.
- Validates stock names and quantities.
- Optionally saves the portfolio summary to a text file.

## Technologies Used
- Python 3

## Concepts Used
- Dictionaries
- Loops
- Conditional statements
- User input and output
- Arithmetic operations
- File handling

## Supported Stocks

| Stock Symbol | Price per Share |
|---|---:|
| AAPL | ₹230 |
| TSLA | ₹250 |
| GOOGL | ₹180 |
| MSFT | ₹420 |
| AMZN | ₹200 |

*Note: These are predefined example prices used by the program, not live market prices.*

## How to Run
1. Install Python 3.
2. Open the terminal in the project folder.
3. Run the following command:

```bash
python stock_tracker.py
```

## How to Use
1. Enter a stock symbol, such as `AAPL`.
2. Enter the quantity of shares.
3. Continue adding stocks as needed.
4. Type `done` to finish entering stocks.
5. View the investment summary.
6. Choose whether to save the results to `portfolio.txt`, if prompted.

## Sample Calculation

```text
AAPL: 10 shares × ₹230 = ₹2,300
TSLA: 5 shares × ₹250 = ₹1,250

Total Investment = ₹3,550
```

## Project Purpose
This project demonstrates how Python can be used to track a basic stock portfolio using dictionaries, calculations, input validation, and file handling.
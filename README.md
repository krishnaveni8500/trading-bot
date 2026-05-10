# Binance Trading Bot

## Project Overview

This project is a Python-based trading bot that connects with the Binance Testnet API and allows users to place cryptocurrency orders from the command line.

The bot supports:

- MARKET Orders
- LIMIT Orders
- BUY and SELL operations
- Input validation
- Logging
- Error handling

This project was built for learning API integration and trading bot development using Python.

---

# Technologies Used

- Python
- Binance API
- python-binance
- python-dotenv
- Logging Module

---

# Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── .env
├── bot.log
├── requirements.txt
└── README.md

---

# Features

## 1. MARKET Orders

Executes buy or sell orders immediately at the current market price.

Example:

- MARKET BUY
- MARKET SELL

---

## 2. LIMIT Orders

Places orders at a custom price specified by the user.

Example:

- Buy BTC at 80000
- Sell BTC at 85000

---

## 3. BUY and SELL Support

The bot supports both buying and selling cryptocurrency.

---

## 4. Validation

User inputs are validated to prevent invalid order types and invalid order sides.

---

## 5. Logging

All successful orders and errors are stored in:

bot.log

---

# Setup Instructions

## Step 1 — Clone or Download Project

Download the project folder.

---

## Step 2 — Install Dependencies

Run:

```bash
python -m pip install -r requirements.txt

## Step 3 — Create .env File

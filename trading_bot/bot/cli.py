

from orders import market_order, limit_order
from validators import (
    validate_side,
    validate_order_type
)

symbol = input("Enter Symbol: ").upper()

order_type = input("Enter MARKET or LIMIT: ").upper()

if not validate_order_type(order_type):

    print("Invalid Order Type")
    exit()


side = input("Enter BUY or SELL: ").upper()

if not validate_side(side):

    print("Invalid Side")
    exit()


quantity = input("Enter Quantity: ")


# MARKET ORDER
if order_type == "MARKET":

    market_order(symbol, side, quantity)


# LIMIT ORDER
elif order_type == "LIMIT":

    price = input("Enter Price: ")

    limit_order(symbol, side, quantity, price)


from client import client
from logging_config import logger


# MARKET ORDER
def market_order(symbol, side, quantity):

    try:

        order = client.create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )

        logger.info(f"Market Order Success: {order}")

        print("\nMARKET ORDER SUCCESS")
        print("Symbol:", order['symbol'])
        print("Order ID:", order['orderId'])
        print("Status:", order['status'])
        print("Type:", order['type'])
        print("Side:", order['side'])
        print("Executed Quantity:", order['executedQty'])

    except Exception as e:

        logger.error(f"Market Order Error: {e}")

        print("Error:", e)


# LIMIT ORDER
def limit_order(symbol, side, quantity, price):

    try:

        order = client.create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            quantity=quantity,
            price=str(price),
            timeInForce='GTC'
        )

        logger.info(f"Limit Order Success: {order}")

        print("\nLIMIT ORDER SUCCESS")
        print("Symbol:", order['symbol'])
        print("Order ID:", order['orderId'])
        print("Status:", order['status'])
        print("Type:", order['type'])
        print("Side:", order['side'])
        print("Price:", order['price'])

    except Exception as e:

        logger.error(f"Limit Order Error: {e}")

        print("Error:", e)
def validate_side(side):

    if side not in ["BUY", "SELL"]:

        return False

    return True


def validate_order_type(order_type):

    if order_type not in ["MARKET", "LIMIT"]:

        return False

    return True
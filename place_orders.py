
# Place an order
try:
    order_id = kite.place_order(tradingsymbol="INFY",
                                exchange=kite.EXCHANGE_NSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=1,
                                order_type=kite.ORDER_TYPE_MARKET,
                                product=kite.PRODUCT_NRML)

    logging.info("Order placed. ID is: {}".format(order_id))
except Exception as e:
    logging.info("Order placement failed: {}".format(e.message))

# Fetch all orders
kite.orders()

# Get instruments
kite.instruments()

# Place an mutual fund order
kite.place_mf_order(
    tradingsymbol="INF090I01239",
    transaction_type=kite.TRANSACTION_TYPE_BUY,
    amount=5000,
    tag="mytag"
)

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if orders.empty:
        return pd.DataFrame({'customer_number': []})

    order = orders.groupby('customer_number')['order_number'].count()
    top_customer = order.idxmax()
    return pd.DataFrame({'customer_number': [top_customer]})
import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate = delivery[delivery['order_date']==delivery['customer_pref_delivery_date']]
    total = len(delivery)
    immediate_count = len(immediate)
    percentage = round(immediate_count / total * 100, 2)
    return pd.DataFrame({'immediate_percentage': [percentage]})
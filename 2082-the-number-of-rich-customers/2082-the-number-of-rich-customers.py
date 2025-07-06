import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    filtered = store[store['amount'] > 500]
    unique_customers = filtered['customer_id'].nunique()
    return pd.DataFrame({'rich_count': [unique_customers]})
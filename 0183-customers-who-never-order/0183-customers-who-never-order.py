import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orderids = orders['customerId'].unique()
    
    cus_df = customers[~customers['id'].isin(orderids)]

    return cus_df[['name']].rename(columns={'name': 'Customers'})
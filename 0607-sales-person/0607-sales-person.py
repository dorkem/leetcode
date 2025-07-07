import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red_com_id = company[company['name'] == 'RED']['com_id'].values
    red_sales_ids = orders[orders['com_id'].isin(red_com_id)]['sales_id'].unique()
    result = sales_person[~sales_person['sales_id'].isin(red_sales_ids)][['name']]
    return result
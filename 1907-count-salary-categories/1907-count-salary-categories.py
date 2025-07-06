import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = accounts[accounts['income']<20000]
    average = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]
    high = accounts[accounts['income']>50000]

    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [len(low), len(average), len(high)]
    })
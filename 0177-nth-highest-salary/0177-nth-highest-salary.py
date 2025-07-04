import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    sorted_df = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if N > len(sorted_df):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    n = sorted_df.iloc[N-1]

    return pd.DataFrame({f'getNthHighestSalary({N})': [n]})
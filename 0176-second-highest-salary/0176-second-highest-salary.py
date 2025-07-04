import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    second_salary = employee["salary"].drop_duplicates().sort_values(ascending=False)
    if len(second_salary) <= 1:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    else:
        return pd.DataFrame({"SecondHighestSalary": [second_salary.iloc[1]]})
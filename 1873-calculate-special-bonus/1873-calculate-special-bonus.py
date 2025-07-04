import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    con1 = employees['employee_id'] % 2 == 1
    con2 = ~employees['name'].str.startswith('M')

    employees['bonus'] = employees['salary'].where(con1 & con2, 0)

    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')
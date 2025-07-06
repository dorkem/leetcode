import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    grouped = employees.groupby(['emp_id', 'event_day'])['total_time'].sum().reset_index()
    grouped.rename(columns={'event_day': 'day'}, inplace=True)

    return grouped[['day', 'emp_id', 'total_time']]

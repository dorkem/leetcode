import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    report_counts = employee.groupby('managerId').size().reset_index(name = 'report_count')
    
    managers = report_counts[report_counts['report_count']>=5]

    result = pd.merge(managers, report_counts, left_on='managerId', right_on='id')[['name']]
    return result
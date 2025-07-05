import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salaries = employee.groupby('departmentId')['salary'].max()
    top_employees = pd.merge(employee, max_salaries, on=['salary', 'departmentId'])
    merged = pd.merge(top_employees, department, left_on = 'departmentId', right_on = 'id')
    return merged[['name_y', 'name_x', 'salary']].rename(
        columns = {
            'name_y': 'Department',
            'name_x': 'Employee'
    })
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    numbers = courses.groupby('class').count()
    numbers = numbers[numbers['student'] >= 5]
    return numbers.reset_index()[['class']]
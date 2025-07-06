import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    teacher_df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    teacher_df.rename(columns={'subject_id': 'cnt'}, inplace=True)
    return teacher_df
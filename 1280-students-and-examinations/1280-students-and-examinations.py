import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    crossed = pd.merge(students, subjects, how = 'cross')
    
    counted = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    merged = pd.merge(crossed, counted, on=['student_id', 'subject_name'], how='left').fillna(0)
    merged['attended_exams'] = merged['attended_exams'].astype(int)
    result = merged.sort_values(by=['student_id', 'subject_name'])

    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']]

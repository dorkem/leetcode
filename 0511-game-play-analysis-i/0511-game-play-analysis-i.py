import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity_sorted = activity.sort_values(by='event_date').drop_duplicates(subset='player_id', keep='first')
    return activity_sorted[['player_id', 'event_date']].rename(columns={
        'event_date': 'first_login'
    })
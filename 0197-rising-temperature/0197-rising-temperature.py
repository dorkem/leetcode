import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')

    weather['pre'] = weather['temperature'].shift(1)

    result = weather[weather['temperature'] > weather['pre']][['id']]

    return result
import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    bull_count = files['content'].str.contains(r'\sbull\s').sum()
    bear_count = files['content'].str.contains(r'\sbear\s').sum()
    
    result = pd.DataFrame({
        'word': ['bull', 'bear'],
        'count': [bull_count, bear_count]
    })

    return result
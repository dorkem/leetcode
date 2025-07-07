import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    round_scores = rounds.groupby('interview_id')['score'].sum().reset_index()

    merged = pd.merge(candidates, round_scores, on="interview_id", how="left")

    result = merged[(merged["years_of_exp"] >= 2) & (merged["score"] > 15)]

    return result[['candidate_id']]
import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads['clicked'] = ads['action'] == 'Clicked'
    ads['not_ignored'] = ads['action'] != 'Ignored'
    
    grouped = ads.groupby('ad_id')[['clicked', 'not_ignored']].sum().reset_index()
    grouped['ctr'] = round(grouped['clicked']/grouped['not_ignored']*100, 2)

    grouped.fillna(0, inplace = True)
    return grouped[['ad_id', 'ctr']].sort_values(by = ['ctr', 'ad_id'], ascending = [False, True])
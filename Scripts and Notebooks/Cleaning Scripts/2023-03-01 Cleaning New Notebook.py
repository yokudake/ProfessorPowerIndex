# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:53:37 2023

@author: kelly
"""

import numpy as np
import pandas as pd

author_df = pd.read_csv(r"G:\My Drive\BrainStation\BrainStationCapstone\Scripts and Notebooks\Raw Data\2023-03-03 Export\author_PoPMetrics_V1.csv")
df = pd.read_csv(r"G:\My Drive\BrainStation\BrainStationCapstone\Scripts and Notebooks\Raw Data\2023-03-03 Export\results_PoPCites_V1.csv",low_memory = True)
cites = df.loc[:, 'Cites'].values

# Get the number of rows 
rows, cols = df.shape

# Get indexs for start and stop
start_list = [0]
end_list = []

for i in range(rows):
    j = i + 1
    if j >= rows:
        break
    else:
        if cites[j]-cites[i] > 0:
            end_list.append(i)
            start_list.append(j)

end_list.append(rows)

au_rows, au_cols = author_df.shape

# Assign query_ids
query_id = np.zeros(rows)
for i in range(au_rows):
    start, stop = start_list[i], end_list[i]+1
    query_id[start:stop] = i

# Save query series to df
quer_ser = pd.Series(query_id)
df['query_id'] = quer_ser

df.to_csv(r"G:\My Drive\BrainStation\BrainStationCapstone\Scripts and Notebooks\Raw Data\2023-03-03 Export\full_results_PoPCites_V1.csv")


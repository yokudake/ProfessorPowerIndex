# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 23:09:38 2023

@author: kelly
"""

import numpy as np
import pandas as pd

df1 = pd.read_csv(r"G:\My Drive\BrainStation\Capstone\Data\2022-02-27 Export\Profiles and Library Export V2.2 _No page Limit_Complete(1).csv")
df2 = pd.read_csv(r"G:\My Drive\BrainStation\Capstone\Data\2022-02-27 Export\Profiles and Library Export V2.2 _No page Limit_Complete(2).csv")

# Concat datasets
df3 = pd.concat([df1, df2], axis = 0)

# Drop NaN Values for author name and Duplicates
df4 = df3.drop(df3[df3['author_info'].isna()].index, axis = 0).drop_duplicates()

# Remove Duplicate article names 
df5 = df4.drop_duplicates('article_title')

#Remove NaN Values for Article Names
df6 = df5.drop(df5[df5['article_title'].isna()].index, axis = 0)

#Remove NaN Values for journal names 
df7 = df6.drop(df6[df6['journal'].isna()].index, axis = 0)

# Remove NaN Values for h_index
df8 = df7.drop(df7[df7['h_index'].isna()].index, axis = 0)

# Remove the abstract and publisher column (information not necessary)
df9 = df8.drop(['abstract', 'publisher'], axis = 1)


def str2int(row):
    if isinstance(row, float):
        return row
    else:
        return int(row.split(' ')[-1])
    
def date2datetime(row):
    if isinstance(row, str):
        try:
            return pd.to_datetime(row).year
        except:
            return np.nan

# Replace number of citations with floats
df10 = df9.assign(num_citations = df9.apply({'num_citations': str2int}))

# Replace publication year with datetime object for year, replace nondatetime objects with NaN
df11 = df10.assign(publication_year = df10.apply({'publication_date': date2datetime})).drop('publication_date', axis = 1)

# Save to new csv
df11.to_csv(r"G:\My Drive\BrainStation\Capstone\Data\2022-02-27 Export\2023-02-27-Cleaned_V1.csv")


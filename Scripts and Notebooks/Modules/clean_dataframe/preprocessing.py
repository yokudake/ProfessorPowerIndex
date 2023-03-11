# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:38:37 2023

@author: kelly
"""
import pandas as pd
    
def dtype16(df, use_float = True, float_col = ''):
    
    '''
    Changes automatically changes the numeric data type for each column to either int16 or float16
    
    Parameters:
    -----------
    df: The Pandas DataFrame
    use_float: True or False. Default is TRUE
    float_col: name of column with the float (MUST SET use_float = True)
    
    Return:
    ------
    ret: A new dataframe with the edited datatypes
    '''
    assert isinstance(df, pd.core.frame.DataFrame), 'Must have object type pandas.core.frame.DataFrame'
    
    if use_float == True:
        assert isinstance(float_col, str), 'The flaot column must be a string'
    else:
        pass
    
    for i in df.select_dtypes('number').columns:
        if i != float_col: 
            df[i] = df[i].astype('int16')
        elif i == float_col and use_float == True:
            df[i] = df[i].astype('float16')
        
    return df
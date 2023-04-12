# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 17:15:46 2023

@author: kelly
"""

import pandas as pd
import numpy as np

# Plotting
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import make_scorer, precision_score, accuracy_score

# Misc tools
from tqdm.notebook import tqdm
from tempfile import mkdtemp
import os
import inspect
import joblib
import warnings
warnings.filterwarnings("ignore")


# Define a custom scoring function that combines accuracy and precision scores

def custom_score_func(y_val, y_pred):
    '''
    
    This function finds the average of the accuracy score and precision scores to use to find the best
    fitting model in GridSearchCV.
    
    Parameters:
    ---------
    y_val: list 
        Validation set of the input target data, used as the true values.
    y_pred: list
        Predicted labels returned by the classifer.
    
    Return:
    ------
    ret: The accuracy and precision score averaged.
    
    '''
    acc = accuracy_score(y_val, y_pred)
    precision = precision_score(y_val, y_pred, average='weighted')
    return (acc + precision) / 2

custom_score = make_scorer(custom_score_func, greater_is_better = True)


# Read File
ml_df = pd.read_pickle('output/NB3_ml_df.pkl')

# Define features and target colums
X = ml_df.drop('PubTier', axis = 1)
y = ml_df['PubTier']

# Split the data set
X_remainder, X_test, y_remainder, y_test =  train_test_split(X, y, test_size=0.25, random_state = 1)


print('Making Pipe')
#Define estimators

estimators = [
    ('scalar', StandardScaler()),
    ('decomp', PCA()),
    ('model', DecisionTreeClassifier())]

c_vals = np.arange(0.01, 110, 10)
n_comp_vals = np.arange(6, 10, 1)
mss_vals = np.arange(30, 40, 1)
depth_vals = np.arange(1, 10, 1)
n_est_vals = np.arange(10, 500, 50)

# Initiate Pipeline object
cachedir = mkdtemp(dir = r'D:\Git\tmp')
pipe = Pipeline(estimators, memory = cachedir)


## Random forest

print('Random Forest')
# Define parameter grid for grid search
param_grid = [
    {'model': [RandomForestClassifier()],
     'scalar':[StandardScaler()],
     'model__n_estimators': n_est_vals,
     'model__max_depth': depth_vals,
    'model__min_samples_split': mss_vals}]

# Initiate the GridSearchCV object with a 5-fold cross validation
rf_grid = GridSearchCV(pipe, param_grid=param_grid, cv = 5, scoring=custom_score)

# Perform the grid search, fitting the grid search to the training data only
rf_grid.fit(X_remainder, y_remainder)

#save your model or results
joblib.dump(rf_grid, 'rf_BestModel_V04-12.pkl')

## Decision Tree

print('Decision Tree')
# Define parameter grid for grid search
param_grid = [
    {'model': [DecisionTreeClassifier()],
     'scalar':[StandardScaler()],
     'model__max_depth': depth_vals,
    'model__min_samples_split': mss_vals}]

# Initiate the GridSearchCV object with a 5-fold cross validation
dt_grid = GridSearchCV(pipe, param_grid=param_grid, cv = 5, scoring=custom_score)

# Perform the grid search, fitting the grid search to the training data only
dt_grid.fit(X_remainder, y_remainder)

#save your model or results
joblib.dump(dt_grid, 'dt_BestModel_V04-12.pkl')
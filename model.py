#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.nonparametric.smoothers_lowess import lowess
from utility import get_outliers
import pickle  

merged_data_setup = pd.read_csv('joined_exp_data.csv')

loess_data = merged_data_setup.dropna()
loess_data = loess_data[['chem_ID','chem_M','value']]

_,filtered_data = get_outliers(loess_data)

x_vals = filtered_data['chem_M']

y_vals = filtered_data['value']

np.save('x_y_vals',np.array([x_vals,y_vals]))

model = lowess(y_vals,x_vals)

with open("loess_model.pickle",'wb') as f:
    pickle.dump(model,f)
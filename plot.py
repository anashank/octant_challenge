#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utility import get_outliers
import pickle

x_y_vals = np.load('x_y_vals.npy')

plt.scatter(x_y_vals[0],x_y_vals[1])

with open('loess_model.pickle','rb') as f:
    model = pickle.load(f)

plt.plot(model[:,0],model[:,1])

plt.xlabel('Chemical concentration')
plt.ylabel('Luciferase activity')
plt.title('LOESS model fit and original data')

plt.savefig('less_model_output.png')
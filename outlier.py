#!/usr/bin/env python3

import pandas as pd
import numpy as np
import fpdf
from utility import get_outliers

merged_data_setup = pd.read_csv('joined_exp_data.csv')

neg_controls = merged_data_setup[merged_data_setup['chem_ID'] == 'C-1']

outliers,_ = get_outliers(neg_controls)

outlier_wells = outliers['well']

perc_outliers = len(outlier_wells) / len(neg_controls) * 100
    

with open('QC_report.txt','w+') as f:
    f.write('Outlier negative control wells:')
    f.write('\n')
    for well in outlier_wells.values:
        f.write(well)
        f.write('\n')
    f.write('Percentage outliers in negative controls:')
    f.write('\n')
    f.write(str(round(perc_outliers,2)) + '%')
    
    
#!/usr/bin/env python3

import pandas as pd
from string import ascii_uppercase
import numpy as np
import argparse

#Function to preprocess files before joining
def process_data(platemap,data):
    row_col_split = platemap['well'].str.split('([A-Za-z]+)',expand=True)
    platemap_id_split = platemap['Plate_ID'].str.split('([A-Za-z]+)',expand=True)
    data_id_split = data['plate'].str.split('([A-Za-z]+)',expand=True)
    
    platemap[['row','col']] = row_col_split[[1,2]]
    platemap['plate_num'] = platemap_id_split[[2]]
    data['plate_num'] = data_id_split[[2]]
    
    letters_index = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=1)}
    
    platemap['row'] = platemap['row'].map(letters_index)
    platemap['col'] = platemap['col'].str.lstrip('0')
    
    platemap['row']=platemap['row'].astype(int)
    platemap['col']=platemap['col'].astype(int)
    platemap['plate_num'] = platemap['plate_num'].astype(int)
    data['plate_num'] = data['plate_num'].astype(int)
    
    return platemap,data

#Provide input files as command line arguments
my_parser = argparse.ArgumentParser()
my_parser.add_argument('--setup', action='store', type=str, required=True)
my_parser.add_argument('--data', action='store', type=str, required=True)

args = my_parser.parse_args()

platemap = pd.read_csv(args.setup)
data = pd.read_csv(args.data)

#Checking input files for invalid data
req_cols_platemap = ['Plate_ID','chem_ID','chem_M','cell_line','neg_control','pos_control','well']
req_cols_data = ['plate','channel','row','col','value']

check_platemap_cols =  all(c1 in req_cols_platemap for c1 in platemap.columns)
check_data_cols =  all(c2 in req_cols_data  for c2 in data.columns)

if check_platemap_cols is False:
    print("Error, all required column names of setup file not present!")
    exit()

if check_data_cols is False:
    print("Error, all required column names of data file not present!")
    exit()
    
check_platemap_dtypes = {'Plate_ID': 'O',
 'chem_ID': 'O',
 'chem_M': 'float64',
 'cell_line': 'O',
 'neg_control': 'O',
 'pos_control': 'O',
 'well': 'O'}

check_data_dtypes = {'plate': 'O',
 'channel': 'O',
 'row': 'int64',
 'col': 'int64',
 'value': 'int64'}

if dict(platemap.dtypes) != check_platemap_dtypes:
    print("Error, ensure all experimental setup columns have correct data type")
    exit()
if dict(data.dtypes) != check_data_dtypes:
    print("Error, ensure all data columns have correct data type")
    exit()

#Joining experimental setup and raw data files
platemap,data = process_data(platemap,data)
merged_data_setup = pd.merge(platemap,data,on=['row','col','plate_num'])
merged_data_setup.to_csv('joined_exp_data.csv',index=None)
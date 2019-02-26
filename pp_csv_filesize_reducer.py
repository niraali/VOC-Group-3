import dask.dataframe as dd
import pandas as pd
from glob import glob
import os

filepathIn = '../pp-complete.csv'
filepathMiddle = '../pp-middle/output-*.csv'
filepathOut = '../pp-minimised.csv'

# This reads in the CSV and takes only the columns specified.
# It then outputs the CSV in small chunks to save on time and memory usage.
if not os.path.isdir('../pp-middle'):
    os.mkdir('../pp-middle')

header_names = ['Price', 'Date of Transfer', 'Postcode', 'Property Type', 'Old/New', 'Duration', 'PAON', 'SAON',
                    'Street', 'Town/City', 'District', 'County']
df = dd.read_csv(filepathIn, usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13], names=header_names)
nottinghamshire_list = df[(df.County == "NOTTINGHAMSHIRE")]

# def inflation(Price):
#     price * 1.028^


nottinghamshire_list.to_csv(filepathMiddle, index=False, header_first_partition_only=True)

# This takes those filenames and collates them into a single CSV file.
filenames = glob(filepathMiddle)
with open(filepathOut, 'w') as out:
    for fn in filenames:
        print("Reading file " + fn)
        with open(fn) as f:
            out.write(f.read())

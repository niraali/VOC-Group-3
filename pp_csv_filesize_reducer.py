import dask.dataframe as dd
from glob import glob

filepathIn = 'F:/Niraali/Documents/VOC/pp-complete.csv'
filepathOut = 'F:/Niraali/Documents/VOC/pp-minimised.csv'

# This reads in the CSV and takes only the columns specified.
# It then outputs the CSV in small chunks to save on time and memory usage.
df = dd.read_csv('pp-complete.csv', usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13])
df.to_csv('pp-minimised/output-*.csv', index=False)


# This takes those filenames and collates them into a single CSV file.
filenames = glob('pp-minimised/output-*.csv')
with open('pp-minimised.csv', 'w') as out:
    for fn in filenames:
        print("Reading file " + fn)
        with open(fn) as f:
            out.write(f.read())

import dask.dataframe as dd
import pandas as pd

def filterByProperty(county, postcode, houseNumber, fileName):
    df = pd.read_csv(fileName, low_memory=False, index_col=False, encoding='utf-8')
    county_list = df[(df.County == county)]
    postcode_list = county_list[(county_list['Postcode'].str.contains(postcode, na=False))]
    houseNumber_list = postcode_list[(postcode_list.PAON == houseNumber)]

    return houseNumber_list

def filterByDistrict(district, fileName):
    df = pd.read_csv(fileName, low_memory=False, index_col=False, encoding='utf-8')
    district_list = df[(df.District == district)]

    return district_list
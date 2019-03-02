import pandas as pd

def filterByProperty(county, postcode, houseNumber, fileName):
    df = pd.read_csv(fileName, low_memory=False, index_col=False, encoding='utf-8', thousands=',')
    county_list = df[(df.County == county)]

    postcode = postcode.strip()                 # Removes any white space after postcode input
    if (' ' in postcode) == False:              # Checks if there are 2 parts to the postcode
        postcode_start = postcode + ' '         # Search by the exact start which requires a space to separate
        postcode_list = county_list[(county_list['Postcode'].str.startswith(postcode_start, na=False))]
        # which line in the postcode input begins with exact string
    else:
        postcode_list = county_list[(county_list['Postcode'].str.contains(postcode, na=False))]
        # otherwise, it looks for if it contains part of the string
    if houseNumber:
        houseNumber_list = postcode_list[(postcode_list.PAON == houseNumber)]
        # Checks if a house number has been entered
        return houseNumber_list
    else:
        return postcode_list
        # if not entered, it just returns the postcode list
def filterByDistrict(district, fileName):
    df = pd.read_csv(fileName, low_memory=False, index_col=False, encoding='utf-8', thousands=',')
    district_list = df[(df.District == district)]

    return district_list


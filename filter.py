from pandas import read_csv, Series
import dask.dataframe as dd


def filter(fileName):
    if fileName == "":
        print("Error")
    else:
        data = read_csv(fileName, names=['price','date_time','post_code','h_type','Q','land_free','number','building_name','street_name','town','city','borough','county','A','AA'])
        # print (data)
        # print (data.head())
        # Create a python list of booleans which tell us which rows match
        # provided post codes
        data.drop('building_name', axis=1, inplace=True)
        data.drop('A', axis=1, inplace=True)
        data.drop('AA', axis=1, inplace=True)

        # Filter for specified price
        booleans = []
        for price in data.price:
            if int(price) >= 110000:
                booleans.append(True)
            else:
                booleans.append(False)

        # print (booleans[0:6])
        # Filter for County
        booleans2 = []
        for county in data.county:
            if county == 'GREATER LONDON':
                booleans2.append(True)
            else:
                booleans2.append(False)

        # Filter for Postcode
        booleans3 = []
        for post_code in data.post_code:
            if post_code == 'HX2 9RX':
                booleans3.append(True)
            else:
                booleans3.append(False)

        # Type of house filter
        booleans4 = []
        for h_type in data.h_type:
            if h_type == 'F':
                booleans4.append(True)
            else:
                booleans4.append(False)

        # Filter for new or old
        booleans5 = []
        for new_old in data.Q:
            if new_old == 'N':
                booleans5.append(True)
            else:
                booleans5.append(False)

        # Filter for land lease or free lease
        booleans6 = []
        for land_free_lease in data.land_free:
            if land_free_lease == 'F':
                booleans6.append(True)
            else:
                booleans6.append(False)

        # Filter for the town
        booleans7 = []
        for town in data.town:
            if town == 'BARLOW':
                booleans7.append(True)
            else:
                booleans7.append(False)

        # Filter for the city
        booleans8 = []
        for city in data.city:
            if city == 'LONDON':
                booleans8.append(True)
            else:
                booleans8.append(False)

        # Filter for the borough
        booleans9 = []
        for borough in data.borough:
            if borough == 'KENSINGTON AND CHELSEA':
                booleans9.append(True)
            else:
                booleans9.append(False)

        booleans10 = []
        for street_name in data.street_name:
            if street_name == 'ALBION STREET':
                booleans10.append(True)
            else:
                booleans10.append(False)


        # Extracting each row where the boolean list is true for each loop
        is_county = Series(booleans2)
        is_post_code = Series(booleans3)
        is_house_type = Series(booleans4)
        is_new_old = Series(booleans5)
        is_land_free_lease = Series(booleans6)
        is_town = Series(booleans7)
        is_city = Series(booleans8)
        is_borough = Series(booleans9)
        is_street_name = Series(booleans10)

        print(data[(data.county == "GREATER LONDON")]) # This is the only line needed to sort by a field
        # print (data[is_post_code])
        # print (data[is_house_type])
        # print (data[is_new_old])
        # print (data[is_land_free_lease])
        # print (data[is_town])
        # print (data[is_city])
        # print (data[is_borough])
        # print (data[is_street_name])
        # print (booleans2)
        # print (is_county)

from statistics import mean
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
from sklearn.model_selection import train_test_split

xs = 0
ys = 0
m = 0
b = 0

def setupData(filename, new, duration, typeOfHouse, postcode):
    global xs, ys, m, b

    data = pd.read_csv(filename)
    # c extracts columns we want
    c = ['Year Sold', 'Property Type', 'New', 'Duration', 'Postcode', 'Present Value (GBP)']
    df = data[c]
    # y is a PV column in integer form
    y = data['Present Value (GBP)'].astype(int)

    # Data Split into train 80%, test 20%, data is randomized in this process
    xTrain, xTest, yTrain, yTest = train_test_split(df, y, test_size=0.2, random_state=0)

    # Pulling out the data where the houses are either new or old
    n_o_data = xTrain[(xTrain['New'] == new)]
    #  pulling out Duration = freehold/leasehold
    duration_data = n_o_data[(n_o_data['Duration'] == duration)]
    # pull out type of house
    type_data = duration_data[(duration_data['Property Type'] == typeOfHouse)]

    # pull out postcode
    end_data = type_data.loc[type_data['Postcode'].str.startswith(postcode, na=False)]
    # TODO: IF DATA IS TOO SHORT SEND ERROR

    # Creating xs as just a year sold column, ys as the PV column
    xs = end_data['Year Sold'].astype(int)
    ys = end_data['Present Value (GBP)'].astype(int)

    m, b = best_fit_slope_and_intercept(xs, ys)

def prototype():
    style.use('ggplot')

    # Print gradient and intercept
    print(m, b)

    # Regression line formula for all x in xs, create a predict_x for desired year 2019
    regression_line = [(m*x)+b for x in xs]
    predict_x = 2019
    predict_y = (m*predict_x)+b
    print(predict_y)

    r_squared = coefficients_of_determination(ys, regression_line)
    print(r_squared)

    return xs, ys, predict_x, predict_y, regression_line

def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig)**2)

# coefficints of determination
def coefficients_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr/ squared_error_y_mean)

# Function to calculated the covariance between xs and ys
def best_fit_slope_and_intercept(xs, ys):
    global m, b
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) / ((mean(xs) * mean(xs)) - mean(xs * xs)))
    b = mean(ys) - m * mean(xs)
    return m, b

def button2(price_input, year_input):
    global xs, ys, m, b

    predict_y = (m * 2019) + b
    intercept = float(price_input) - m * int(year_input)
    intercept_difference = intercept - b
    predict_house = predict_y + intercept_difference
    print(predict_house)
    # house_regression_line = [(m*year_input+a]
    return predict_house

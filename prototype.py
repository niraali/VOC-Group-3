from statistics import mean
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style
from sklearn.model_selection import train_test_split


year_input = 2007
price_input = 975000
is_it_new_input = 'Y'
duration_input = 'L'
property_type_input = 'D'
postcode_input = 'NG2'

style.use('ggplot')
# Input headers myself into this file so i can run code,
data = pd.read_csv('pp-nottinghamshire2.csv', names = ['Year_sold', 'Price', 'PV', 'Postcode', 'PropertyType',
                                'Old_New', 'Duration', 'PAON', 'SAON', 'Street', 'Town_City', 'District', 'County'])
# line 17 is deleting the old header line and removing the comma in the PV line ( this you might not need niraali)
data.drop(data.index[0], inplace=True)

# c extracts columns we want
c = ['Year_sold','PropertyType', 'Old_New', 'Duration', 'Postcode', 'PV']
df = data[c]
# y is a PV column in integer form
y = data['PV'].astype(int)

# Data Split into train 80%, test 20%, data is randomized in this process 
xTrain, xTest, yTrain, yTest = train_test_split(df, y, test_size=0.2, random_state=0)

# Pulling out the data where the houses are either new or old
n_o_data = xTrain[(xTrain.Old_New == is_it_new_input)]
#  pulling out Duration = freehold/leasehold
duration_data = n_o_data[(n_o_data.Duration == duration_input)]
# pull out type of house
type_data = duration_data[(duration_data.PropertyType == property_type_input)]

#pull out postcode
end_data = type_data.loc[type_data['Postcode'].str.startswith(postcode_input, na=False)]
#TODO: IF DATA IS TOO SHORT SEND ERROR

# Creating xs as just a year sold column, ys as the PV column
xs = end_data.Year_sold.astype(int)
ys = end_data.PV.astype(int)

# Function to calculated the covariance between xs and ys
def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) -mean(xs*ys)) / ((mean(xs)*mean(xs)) - mean(xs*xs)))
    
    b = mean(ys) - m*mean(xs)
    

    return m, b
    
m, b = best_fit_slope_and_intercept(xs,ys)
#a = intercept_of_vs(xs,ys,info)
# Print gradient and intercept
print(m,b)


inter = price_input - m*year_input
#ys_line = mx+b
def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig)**2)
# coefficints of determination
def coefficients_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig,y_mean_line)
    return 1 - (squared_error_regr/ squared_error_y_mean)


# Regression line forumla for all x in xs, create a predict_x for desired year 2019
regression_line = [(m*x)+b for x in xs]
predict_x = 2019
predict_y = (m*predict_x)+b
print(predict_y)

intercept_difference = inter - b
predict_house = predict_y + intercept_difference
print(predict_house)
#house_regression_line = [(m*(info[0]))+a]


r_squared =  coefficients_of_determination (ys, regression_line)
print(r_squared)

# Producing the scatter plots between the data xs,ys and then the regression line and the predicted value
plt.scatter(xs,ys, color='#003F72', label='data')
plt.scatter(predict_x, predict_y, color='g', label='Predicted point')
plt.plot(xs, regression_line, label='Regression line')
plt.scatter(year_input,price_input, color='r', label = 'Previous sale')
plt.scatter(predict_x, predict_house, color='g', label='Predict house')
plt.legend(loc=4)
plt.show()
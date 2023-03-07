import pandas as pd
import numpy as np
import random

# Simulate var1
# Purpose : simulates var1 by randomly selecting a level from a list of land-use types (levels).
var1 = []   # create an empty list to store the simulated variable
random.seed(24)      # optional: set the seed of the random number generator to ensure reproducibility
levels = ["Permanent crops", "Irrigated crops", "Managed Forest", "Natural Forest", "Agro-Forestry system", "Urban", "Pasture", "Shrubland" ]
                            # create a list of land-use types to choose from

for _ in range(100):        # repeat the following block of code 100 times
    var1 += random.sample(levels, 1)
                            # randomly select one land-use type from the list and append it to var1
                            # using the `+=` operator to concatenate the list with the new element
                            # var1.append(random.sample(levels, 1)) would also work
# the loop is needed to repeat the process of randomly selecting a land-use type and adding it to the var1 list, 100 times.
# type of var1 = list of strings
#  Visualisation = Fig1 (VAR1 is a categorical variable ==> bar chart)


# # Simulate var2
np.random.seed(24)   # optional: used to fix the seed of the pseudo-random number generator (use any number of your choice)

var2 = np.random.uniform(0, 100, 100)
                           # generate 100 observations of a uniform random variable
                           # between 0 and 100, inclusive
                           # using NumPy's random.uniform() function

# type of var2 = continuous numerical variable
#  Visualisation = Fig2 (Box plot)

# # #Simulate table1
table1 = pd.DataFrame(var1).value_counts(sort=True) 
# turn value of var1  into a Pandas Series
# value_counts() function to count the frequency of each unique value of var1. 
# The sort=True argument sorts the values in descending order of frequency.
table1 = table1.rename_axis("landuse")
table1 = table1.reset_index(name="Frequency")
# table1 is a frequency table using the values generated in var1. 
# The result is a Pandas DataFrame with two columns: landuse and Frequency.
# type of table1  = table contains categorical variable that shows the frequency distribution of var1 in each land use type


# # # # Simulate table2
table2 = pd.DataFrame(list(zip(var1, var2)), columns = ["landuse", "cover"])
# zip() function is used to combine the two variables into a list of tuples, where each tuple contains one land use and its corresponding land cover. 
# Note: The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together, etc. The tuple() function displays a readable version of the result - try running: print(tuple(zip(var1,var2)))
#  Visualisation = Fig3 (scatter plot)




# # # # # Simulate table3
np.random.seed(24) # optional: used to fix the seed of the pseudo-random number generator (use any number of your choice)
year = list(range(1970,2021)) # create a list called year containing years from 1970 to 2020.
temp = np.random.normal(17,2,51)
# generate 51 random values using a normal distribution with a mean of 17 and standard deviation of 2. 
# These values represent temperatures for each year in year. 
# The resulting values are stored in a Numpy array called temp.
table3 = pd.DataFrame(list(zip(year, temp)), columns = ["Year", "Temperature"])
# combine the year and temp arrays into a list of tuples using the zip() function. 
#  Visualisation = Fig4 (line chart)


# # # # # # Simulate table4
xx = np.array([16,21])  # define an array xx with two elements, 16 and 21.
yy = np.array([300, 1200]) # define an array yy with two elements, 300 and 1200.
means = [xx.mean(), yy.mean()] # calculate the mean values of the xx and yy arrays and stores them in a list called means. 
stds = [xx.std() / 3, yy.std() / 3] # calculate the standard deviations of the xx and yy arrays, and then divides each by 3. The resulting values are stored in a list called stds.
corr = -0.7 # correlation
covs = [[stds[0]**2          , stds[0]*stds[1]*corr],  
        [stds[0]*stds[1]*corr,           stds[1]**2]] # covariance matrix
table4 = pd.DataFrame(np.random.multivariate_normal(means, covs, 100), columns = ["Mean Anual Temperature", "Total Precipitation"])
# generate a pandas dataframe called table4 with 100 rows and two columns, named "Mean Anual Temperature" and "Total Precipitation". The values in the dataframe are generated using np.random.multivariate_normal(), which generates a set of random samples based on the means, covariance matrix, and size parameters.
# type of data : numerical and continuous
#  Visualisation = Fig5 (scatter plot)




# # # # # # # Simulate table5
col1 = pd.Series(list(range(1900,2010,10))).repeat(8)
# create a pandas series called col1 that contains a sequence of integers ranging from 1900 to 2010, in increments of 10. The repeat(8) method is used to repeat each value 8 times, resulting in a series with 1116 elements.
col2 = ["Permanent crops", "Irrigated crops", "Managed Forest", "Natural Forest", "Agro-Forestry system", "Urban", "Pasture", "Shrubland" ]*11
# create a list called col2 that contains eight land use categories, which are repeated 11 times each using the * operator. The resulting list has a total of 88 elements.
col3 = np.random.uniform(0, 100, 90)
# generate a numpy array col3 with 90 elements, where each element is a random number between 0 and 100, drawn from a uniform distribution.
table5 = pd.DataFrame(list(zip(col1, col2, col3)), columns = ["Year", "Landuse", "Cover"])
# create a pandas dataframe called table5 by combining the three arrays col1, col2, and col3 into a list of tuples using the zip() function. The resulting list of tuples is then used to create the dataframe with the column names "Year", "Landuse", and "Cover".
# type of data : combination of categorical and numerical data. 
# The "Landuse" column contains categorical data
# the "Year" column contains discrete numerical data
# the "Cover" column contains continuous numerical data.
#  Visualisation =  heatmap with the year on the x-axis and the land use category on the y-axis, with the cell values representing the percentage of land covered.
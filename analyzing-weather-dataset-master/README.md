Problem Statement
We'll be working with a csv file that contains weather data for each hour in 2012. There are many interesting connections between everyday life and the weather that we will explore with the help of this dataset. Apply all the numpy and pandas skills learned so far to analyze the data.

About the Dataset-
Snapshot of the Dataset:

![Screenshot (524)](https://user-images.githubusercontent.com/60145175/115015000-ac895680-9ed0-11eb-9ed1-c4facf1e36da.png)

# Features:

![Screenshot (525)](https://user-images.githubusercontent.com/60145175/115015050-bdd26300-9ed0-11eb-9cdc-1570b3aae232.png)


# Task
## Instructions
Different functions that you would require to define for this project has been mentioned in the code block. All the parameters and the task, a function would do, have been mentioned there.

* Load the weather_2012 data csv file and store it in weather variable. The path of the dataset has been stored in the variable path for you.
* Check the categorical and numerical variables. You can check it by calling categorical and numerical functions.
* Check the distribution of a specific value like the number of times the weather was exactly Cloudy in the given column. Feel free to check on other values. You can check it by calling the function clear with respective parameters.
* By using the index of the value or name of the value you can check the number of counts. Now suppose you want to check some instances based on a specific condition like when the wind speed was above 35 and visibility was 25. You can directly check it by calling the function instances_based_condition with respective parameters and store the resulting dataframe in wind_speed_35_vis_25.
* You have temperature data and want to calculate the mean temperature recorded by month. You can generate a pivot table that contains the aggregated values(like mean, max, min, sum, len) recorded by month. You can call the function agg_values_ina_month with respective parameters.
* To groupby based on a column like you want to groupby on Weather column and then aggregate the mean values of each column for different types of weather using mean. You can call the function group_values and store the resulting dataframe in mean_weather. Feel free to try on different aggregated functions like max, min, sum, len
* You want to convert Celsius temperature into Fahrenheit temperatures. Call the function convert to do the same.

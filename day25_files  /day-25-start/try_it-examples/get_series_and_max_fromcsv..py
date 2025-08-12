"""---Another Challenge---

Objective: Find the max in the list using Series class from the pandas library
"""
import pandas as pds


data = pds.read_csv("/Users/kgreen/PycharmProjects/PYLEARNING/day25_files  /day-25-start/weather_data.csv")


data_dict = data.to_dict()
#print(data_dict)


#temp_list = data["temp"].to_list() #since we are using series let's change temp_list to temp_series. it will no longer be a list

temp_series = data["temp"] 


max_value = temp_series.max()
print(temp_series)
print(f"The max value in the list using Series is {max_value}")

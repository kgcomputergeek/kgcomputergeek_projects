"""---Another Challenge---

Objective: Find the max in the list using Series class from the pandas library
"""
import pandas as pds


data = pds.read_csv("/Users/kgreen/PycharmProjects/PYLEARNING/day25_files  /day-25-start/weather_data.csv")


data_dict = data.to_dict()
#print(data_dict)


#temp_list = data["temp"].to_list() #since we are using series let's change temp_list to temp_series. it will no longer be a list

temp_series = data["temp"] 


#get data in columns
print(data["condition"])
data.condition

#get data in rows
print(data[data.day == "Monday"])

# get data where the row has the highest temp
max_temp = data["temp"].max()
row_with_max_temp = data[data["temp"] == max_temp]
print(f"The row with the max temp is: {row_with_max_temp}")


"""
option 2- is cleaner and deals with less strings

max_temp = data.temp.max()
row_with_max_temp = max_temp
print(f"The row with the max temp is: {row_with_max_temp}")


"""

#get monday stuff
# monday_stuff = data[data.day == "Monday"]
# print(monday_stuff.condition)



#or data[data["day"]]
# max_value = temp_series.max()
# print(temp_series)
# print(f"The max value in the list using Series is {max_value}")


"""
cel to fah conversion
"""

# 1. Define the conversion function
def cel_to_fah(cel):
    return (cel * 9/5) + 32

# 2. Specify the day(s) of the week for conversion
target_day = 'Monday' # You can change this to any day or a list of days
 #Create a new column for fah temperature (optional, but good practice)
# Initialize it with NaN or copy cel values if you want to convert in place later
data['temp_fah'] = pds.NA # Or data['temp_fah'] = data['temp']

# 4. Identify rows for the target day(s)
is_target_day = data['day'] == target_day

# 5. Apply the conversion to the 'temp' column for the target day(s)
# and store it in the 'temp_fah' column for those specific rows.
data.loc[is_target_day, 'temp_fah'] = data.loc[is_target_day, 'temp'].apply(cel_to_fah)

# If you want to fill fah for other days as well (e.g., if they were already in F or just copy C)
# For this example, let's assume non-target days' fah column remains NA or you could fill them appropriately.
# For instance, if you wanted all days converted, you'd skip the filtering:
# data['temp_fah'] = data['temp'].apply(cel_to_fah)


# Print the DataFrame to see the changes
print(f"DataFrame after converting temperatures for {target_day} to fah:")
print(data)

# If you only want to see the rows for the target day with the new temperature
print(f"\nTemperatures for {target_day}:")
print(data[is_target_day][['day', 'temp', 'temp_fah', 'condition']])
# 3.


"""
create a dataframe from scratch

"""
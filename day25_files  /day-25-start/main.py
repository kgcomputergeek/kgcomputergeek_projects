import pandas as pds

weather_data = pds.read_csv("/Users/kgreen/PycharmProjects/PYLEARNING/day25_files  /day-25-start/weather_data.csv")


# print(weather_data.head()) #displays first few rows of the data frame

# print(weather_data.columns) #displays column names


# Step 2: Rename columns
weather_data.rename(columns={"day": "Day of the Week"}, inplace=True)
weather_data.rename(columns={"temp": "Temperature"}, inplace=True)
weather_data.rename(columns={"condition": "Weather Condition"}, inplace=True)

print("Renamed DataFrame:")
print(weather_data)

"""
# Step 3: Write the updated DataFrame to a new text file
weather_data.to_csv("renamed_weather_data.txt", index=False, sep="\t")

print("Data with renamed columns saved to 'renamed_weather_data.txt'.")

"""

"""
import pandas as pd

# Step 1: Load the CSV file
weather_data = pd.read_csv("weather_data.csv")

# Step 2: Explore the data
print("Full DataFrame:")
print(weather_data)

# Step 3: Access specific columns
print("\nTemperature Data:")
print(weather_data["Temperature"])

# Step 4: Perform analysis or filtering
# Example: Filter days with temperature > 15
warm_days = weather_data[weather_data["Temperature"] > 15]
print("\nWarm Days (Temperature > 15):")
print(warm_days)

# Example: Average temperature
average_temperature = weather_data["Temperature"].mean()
print("\nAverage Temperature:")
print(average_temperature)



"""
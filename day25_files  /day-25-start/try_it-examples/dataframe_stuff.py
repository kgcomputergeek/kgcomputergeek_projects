# import pandas as pds
# import math as ma

# data = pds.read_csv("/Users/kgreen/PycharmProjects/PYLEARNING/day25_files  /day-25-start/weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)


# temp_list = data["temp"].to_list()

# #find the average temperature

# avg = sum(temp_list)/len(temp_list)
# avg_round = round(avg, 2)
# #req_results = f"The average temperature is {avg}"
# print(f"The average temperature is {avg:.0f}") #best and takes output from 17.428571428571 to a neater one


"""

---Another Challenge---

Objective: Find the max in the list using Series class from the pandas library
"""
# import pandas as pds


# data = pds.read_csv("/Users/kgreen/PycharmProjects/PYLEARNING/day25_files  /day-25-start/weather_data.csv")


# data_dict = data.to_dict()
# #print(data_dict)


# #temp_list = data["temp"].to_list() #since we are using series let's change temp_list to temp_series. it will no longer be a list

# temp_series = data["temp"] 


# max_value = temp_series.max()
# print(temp_series)
# print(f"The max value in the list using Series is {max_value}")

"""
Create a dataframe from scratch

"""
import pandas as pd

df_dict = {
    "estudiantes": ["Roberta" , "Jaime" , "Angelo"],
    "puntajes": [84,97,56]
}
df = pd.DataFrame(df_dict)
df.to_csv("data_nueva.csv")
# df_csv = df.to_csv(df_dict)
# print(df_csv)
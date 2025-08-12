"""
Objective: Find count for each of the following squirrel colors and have that output into a csv file called "squirrel_count.csv" :

Grey
Red(aka Cinnamon)
Black

Steps: 

1. Extract data from csv by declaring a variable to read the csv file 
2. then make a seperate variable for each color to print the count using the len() method. Each color can be found in the "Primary Fur Color" column
3. Create a dictionary with key value pairs with the Keys being, "Fur Color" and "Count" and Values for each. Ex: Count (grey_sq_count)
    "Fur Color":
    "Count":

4. Place the keys
"""

import pandas as pa

data_extract = pa.read_csv("/Users/kgreen/PycharmProjects/PYLEARNING/day25_files  /squirrel_assign/2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")

#find count of each color type
grey_sq_ct = len(data_extract[data_extract["Primary Fur Color"]== "Gray"])
red_sq_ct = len(data_extract[data_extract["Primary Fur Color"]== "Cinnamon"])
blk_sq_ct = len(data_extract[data_extract["Primary Fur Color"]== "Black"])

print(grey_sq_ct)
print(red_sq_ct)
print(blk_sq_ct)

data_extract_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_sq_ct,red_sq_ct,blk_sq_ct]

}

df = pa.DataFrame(data_extract_dict)
df.to_csv("squirrel_count.csv")








"""

import pandas as pd

# 1) Read the original CSV
df = pd.read_csv("/Users/kgreen/PycharmProjects/PYLEARNING/day25_files  /squirrel_assign/2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")

# 2) Count squirrels by fur color



# Method A: using value_counts()
# counts = (
#     df['Primary Fur Color'] #returns a series indexed by color, with counts as values with columns index (the color) and FurColor (the count).
#     .value_counts() #counts the fur color values (aka how many of each color)
#     .reset_index() #turns intp DF with the columns index 
#     .rename(columns={'index': 'Primary Fur Color', 'Primary Fur Color': 'Count'}) #renames columns to Primary
# )



counts = (
   df
   .groupby('Primary Fur Color')
   .size()
   .reset_index(name='Count')
)

# 3) Write the counts to a new CSV
counts.to_csv('squirrel_count.csv', index=False)

print(counts)
"""

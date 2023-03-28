# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    data_list = list(data)

    temperature = []
    for row in data_list[1:]:
        temperature.append(int(row[1]))
    print(temperature)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

# use sum of list / len of list to get mean
temp_list = data["temp"].to_list()
print(temp_list)

avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

# use series (numpy) to execute calculation
avg_temp_series = data["temp"].mean()
print(avg_temp_series)

print(data["condition"])
# pandas takes each column and its heading as an attribute to dataframe
print(data.condition)

monday = data[data["day"] == "Monday"]
monday_temp = int(monday["temp"])
monday_temp_to_fer = monday_temp * 9 / 5 + 32
print(monday_temp_to_fer)

student_dict = {"Name": ["Amy", "Brandon", "Carl"],
                "Sex": ["female", "male", "male"],
                }

student_df = pd.DataFrame(student_dict)
print(student_df)
student_df.to_csv("student_data.csv")

import pandas as pd
import prettytable

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# check for row and columns
print(squirrel_data)

# use pretty table to summarize column_name, data_type and NaN values
table = prettytable.PrettyTable()
table.add_column("column_name", squirrel_data.columns)
table.add_column("data_type", squirrel_data.dtypes)
table.add_column("sum_of_NaN_values", squirrel_data.isna().sum())
print(table)

# or use df.info() to print out overview of all the dtypes used in dataframe, along with its shape and other information
# squirrel_data.info()

# count for different values in "Primary Fur Color"
fur_data = squirrel_data["Primary Fur Color"].value_counts()
print(fur_data)

# reset index and columns to prepare data for new csv file
fur_data = fur_data.rename_axis("Fur Color")
print(fur_data)
new_fur_data = fur_data.reset_index(name='Counts')
print(new_fur_data)

# output the information we wanted as another csv file
new_fur_data.to_csv("squirrel_color_count.csv")


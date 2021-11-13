import pandas as pd

# a = [1,2,3,4,5]

# my_series = pd.Series(a)

# print(my_series)
# print(type(my_series))

# #create custom index
# my_series = pd.Series(a, index=["A", "B", "C", "D", "E"])
# print(my_series)

# # or
# my_series = pd.Series(a, index=[{"A":1, "B":2, "C":3, "D":4, "E":5}])
# print(my_series)

# Data frame

# data = {
#     "Duration": [50,60,70],
#     "Calories": [123, 344, 500]
# }

# my_df = pd.DataFrame(data)
# print(my_df)
# my_df.to_csv("my_df.csv", index=False)


my_df = pd.read_csv("cars1.csv")
print(my_df.head(10))
print(my_df.tail(5))

# print row 5 from my_df
print(my_df.loc[5]) 

# print row 5 and row 10 from my_df
print(my_df.loc[[5,10]])

#changing index using column 
my_df = pd.read_csv("cars1.csv", index_col="RegNum")

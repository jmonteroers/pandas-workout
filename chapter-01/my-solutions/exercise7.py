import pandas as pd
import numpy as np

# Load taxi distances into Series
s_d = pd.read_csv("data/taxi-distance.csv", header=None).squeeze()

# Classify distances into short, medium, and long
s_d_cat = pd.Series("Medium", index=s_d.index)
s_d_cat.loc[s_d > 10] = "Long"
s_d_cat.loc[s_d <= 2] = "Short"

# Counts per categories
print(s_d_cat.value_counts())

# Suggested: use pd.cut (by default, bins include the rightmost edge)
s_d_cat2 = pd.cut(
    s_d, bins=[0, 2, 10, np.inf], 
    include_lowest=True,
    labels=["Short", "Medium", "Long"])
print(s_d_cat2.value_counts())


"""
Beyond the Exercise, Question 1:
Compare the mean and median trip distances. 
What does the comparison tell you about the distribution of the data?

The mean is much larger than the median, indicating right-skewedness
"""
print(s_d.describe())

"""
Beyond the Exercise, Question 2:
Count the number of short, medium, and long trips for trips that had only one passenger. 
Note: The data for passenger count and trip length comes from the same data set, meaning the indexes align.
"""
s_p = pd.read_csv("data/taxi-passenger-count.csv", header=None).squeeze()

print(s_d_cat2.loc[s_p == 1].value_counts())

"""
Beyond the Exercise, Question 3:
What happens if you don't pass explicit intervals to `pd.cut` 
and instead ask it to create three bins using `bins=3`?

If int, it creates equal-width bins based on the range of the series,
extended by 0.1% on each side to include the min/max
"""
s_d_cat3 = pd.cut(
    s_d, bins=3, 
    include_lowest=True,
    labels=["Short", "Medium", "Long"])
print(s_d_cat3.value_counts())

# To reproduce the count in the first bin
stat_range = s_d.max() - s_d.min()

# count, first interval
count_first_interval = s_d.loc[s_d <= (s_d.min() - 0.001*stat_range + 1.002/3.*stat_range)].shape[0]
print(f"Count, First interval of automatic pd.cut: {count_first_interval}")
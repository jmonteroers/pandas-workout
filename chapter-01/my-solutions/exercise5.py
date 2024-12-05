"""
Ex 5. Use a Series index to get average temperature on Monday over a month
"""

import pandas as pd
import numpy as np


LUCKY_NUMBER = 0

g = np.random.default_rng(LUCKY_NUMBER)


dow = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

s = pd.Series(
    g.normal(20., 5., 28), index=4*dow
)
s = s.round()

print(s.head(10))
print(f"Overall mean: {s.mean():2.2f}")
print(f"Monday mean: {s.loc["Mon"].mean():2.2f}")


"""
5.1. What was the average weekend temperature (i.e., Saturdays and Sundays)? 
"""
print(f"Weekend mean: {s.loc[["Sat", "Sun"]].mean():2.2f}")

"""
5.2. How many times is the change in temperature from the previous day greater than 2 degrees? 
"""
diff_temps = s.diff()
print(f"# times large diff temp: {(diff_temps > 2.0).sum():d}")

# suggested, more clear when these diffs take place
print(s.loc[s.diff() > 2.])

"""
5.3. What are the two most common temperatures in our data set, and how often does each appear?
"""
print(s.value_counts(ascending=False))
# suggested, to add .head(2) to show only two temps
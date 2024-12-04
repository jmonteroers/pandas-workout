"""
Calculating descriptive statistics
"""

import numpy as np
import pandas as pd

LUCKY_NUM = 8

g = np.random.default_rng(LUCKY_NUM)

s = pd.Series(
    g.normal(0, 100, 100_000)
)

print(s.describe())

# Modify min to 5 times maximum
s.loc[s.idxmin()] = 5 * s.max()

print(s.describe())

"""
1. Show that (approx) 68%, 95%, and 99.7% of the values in s are indeed within one, two, and three standard distributions of the mean.
"""
avg_s = s.mean()
std_s = s.std(ddof=0)

def prop_within_sd(s, avg, std, n):
    return ((s - avg).abs() <= n * std).mean()

within_one = prop_within_sd(s, avg_s, std_s, 1)
within_two = prop_within_sd(s, avg_s, std_s, 2)
within_three = prop_within_sd(s, avg_s, std_s, 3)

print(f"""
--- Proportions close to the mean ---
- Within 1 SD, {within_one:2.2%}
- Within 2 SD, {within_two:2.2%}
- Within 3 SD, {within_three:2.2%}
""")

"""
2. Calculate the mean of numbers greater and lower than the mean. Is the average of these two numbers the same as s.mean()?
NO
"""

avg_below_mean = s.loc[s < s.mean()].mean()
avg_above_mean = s.loc[s > s.mean()].mean()
avg_below_above = (avg_below_mean + avg_above_mean) / 2.
print(
    f"Original mean {avg_s:1.3f}, while mean of means {avg_below_above:.3f} "
    f"({avg_below_mean:0.3f}, {avg_above_mean:0.3f}) with sample size "
    f"({(s < s.mean()).sum():d}, {(s > s.mean()).sum():d})"
      )

"""
3. What is the mean of the numbers beyond three standard deviations?
"""
avg_beyond_three = s.loc[(s - avg_s).abs() > 3 * std_s].mean()
print(f"Average beyond 3 SD: {avg_beyond_three:4.2f}")
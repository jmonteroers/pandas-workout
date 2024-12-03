"""Beyond the exercise 
1. What if the range were from 0 to 10,000? How would that change your strategy, if at all? 
"""
import numpy as np
import pandas as pd

LUCKY_SEED = 8
g = np.random.default_rng(LUCKY_SEED)

nums = pd.Series(g.integers(0, 10000, 10))

tens = nums % 100 // 10

print("--- Original Nums ---")
print(nums)
print("--- Tens ---")
print(tens)

"""
2. Given a range from 0 to 10,000, what's the smallest dtype you should use for integers? 
np.int16
"""
# Absolutely fails
# s1 = pd.Series([10000], dtype=np.int8)
print("This works")
s2 = pd.Series([10000], dtype=np.int16)
print(s2)

"""
3. Create a new series with 10 floating-point values between 0 and 1,000. Find the numbers whose integer component (i.e., ignoring any fractional part) are even.
"""
float_nums = pd.Series(
    1000.*g.random((10,))
)
print("--- Float numbers ---")
print(float_nums)
print("--- Selected floats w even integer part ---")
print(float_nums.loc[float_nums.astype(np.int16) % 2 == 0])
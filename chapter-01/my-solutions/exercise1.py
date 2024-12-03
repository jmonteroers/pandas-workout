import pandas as pd
from calendar import month_abbr
from numpy.random import default_rng

LUCKY_SEED = 8

# Generate course months
month_nums = list(range(9, 13)) + list(range(1, 7))
course_months = [month_abbr[n] for n in month_nums]

# Generate results by months
g = default_rng(LUCKY_SEED)
grades = g.integers(70, 101, 10)
print(grades.shape)

# Create series
s = pd.Series(grades, index=course_months)

## Analyse scores
avg_year = s.mean()

# Slicing
# one option, less readable (commented out)
# avg_first_half = s.iloc[:5].mean()
# avg_second_half = s.iloc[5:].mean()

# can also use intervals delimited by index values
# NOTE: with loc, end value is included
avg_first_half = s.loc['Sep':'Jan'].mean()
avg_second_half = s.loc['Feb':].mean()

diff = avg_second_half / avg_first_half - 1.

print(f"""----Test results----
Y: {avg_year: 2.2f}
H1: {avg_first_half: 2.2f}
H2: {avg_second_half: 2.2f}
Difference H1-H2 (%): {diff:2.2%}
""")

# Beyond
print(s)
# Month, highest score
print(s.idxmax())
# Top 5 scores
print(s.sort_values(ascending=False).head(5))
# Round to nearest 10
print(s.round(-1))
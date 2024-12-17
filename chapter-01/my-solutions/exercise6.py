"""Read csv file, squeeze into Series, and compute odds of taxi rides with 1 passenger vs 6 passengers"""

import pandas as pd

# proposed: header=None to remove Series name
s_t = pd.read_csv("data/taxi-passenger-count.csv", header=None).squeeze()

prop_min_pass = (s_t == 1).mean()
prop_max_pass = (s_t == 6).mean()
odds = prop_min_pass / prop_max_pass

print(
f"""
Prop only 1 passenger: {prop_min_pass:2.2%}
Prop max # passengers (6): {prop_max_pass:2.2%}
Odds: {odds:2.2f}"""
)

# Proposed solution using value_counts
print(s_t.value_counts(normalize=True).loc[[1, 6]])

"""
6.1. What are the 25%, 50% (median), and 75% quantiles for this data set? Can you guess the results before you execute the code?

First two must be 1, 1. For the 75% quantile it is likely 2
"""

print(s_t.quantile([0.25, 0.5, 0.75]))


"""
6.2. What proportion of taxi rides are for three, four, five, or six passengers?
"""
s_value_counts = s_t.value_counts(normalize=True)
prop_at_least_three = s_value_counts.loc[s_value_counts.index >= 3].sum()
print(f"{prop_at_least_three:2.2%}")

"""
6.3. Consider that you’re in charge of vehicle licensing for New York taxis. Given these numbers, would more people benefit from smaller taxis that can take only one or two passengers or larger taxis that can take five or six passengers?
It would be more efficient to have a fleet of smaller taxis. However, the effect on taxi rides with small numbers of passengers depends on preferences.
"""
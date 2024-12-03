""" Teacher corrects scores to have average 80 """

from calendar import month_abbr
import pandas as pd
import numpy as np

TARGET_AVG = 80.
LUCKY_SEED = 8

course_months = [month_abbr[i] for i in list(range(9, 13))+list(range(1, 7))]
g = np.random.default_rng(LUCKY_SEED)

course_grades = pd.Series(
   g.integers(40, 60, len(course_months)),
   index=course_months
)

correction = TARGET_AVG - course_grades.mean()

corrected_grades = course_grades + correction

print("--- Original Grades ---")
print(course_grades)

print("--- Corrected Grades ---")
print(corrected_grades)

print(f"Applied Correction: {correction:+2.2f}")
print(f"Original Average: {course_grades.mean():2.2f}")
print(f"New Average: {corrected_grades.mean():2.2f}")


""" Beyond the exercise """
"""
Ex1. Map to score letters, using the following info:
if within one sd, B (+), C(-)
beyond, A or D
"""
 
avg_grades = course_grades.mean()
sd_grades = course_grades.std(ddof=0)


def map_grades_to_letter(grade, avg, sd):
    if grade < avg - sd:
        return "D"
    elif grade < avg:
        return "C"
    elif grade < avg + sd:
        return "B"
    return "A"

course_letters = course_grades.map(
    lambda x: map_grades_to_letter(x, avg_grades, sd_grades)
)


print(f"Original Average: {avg_grades:2.2f}")
print(f"Original Std: {sd_grades:2.2f}")

print("--- Letter Grades ---")
print(course_letters)

"""
Ex2. Any scores below or above 2 sds the mean?
"""

def id_extreme_results(grade, avg, sd):
    if grade < avg - 2*sd:
        return "Extreme Low"
    elif grade >  avg + 2*sd:
        return "Extreme High"
    return "Standard"

extreme_res = course_grades.map(
    lambda x: id_extreme_results(x, avg_grades, sd_grades)
)
print("--- Extreme Results ---")
print(extreme_res)

"""
Ex3. Mean vs median
"""
median_scores = course_grades.median()
print(f"Median: {median_scores:2.2f}")
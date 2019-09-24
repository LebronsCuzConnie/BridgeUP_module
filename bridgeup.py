# This document will contain all of the functions in the bridgeup module

# Add a comment at the bottom of the file explaining what your function does 
# and then add your function below

import pandas as pd

df = pd.read_csv("internship_bootcamp_data.csv")

def grade_num(num): 
    grade = df["Grade"]
    total = 0 
    for i in grade: 
        if i == num: 
            total += 1 
    return total

# this function counts the amount of brown scholars in a certain grade. 
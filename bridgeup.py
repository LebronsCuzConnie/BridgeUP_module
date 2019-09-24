# This document will contain all of the functions in the bridgeup module

# Add a comment at the bottom of the file explaining what your function does 
# and then add your function below

import pandas as pd

df = pd.read_csv("internship_bootcamp_data.csv")
df["Grade"]
def grade(brown_scholar):
    gr = df["Grade"].loc[df["First Name"]==brown_scholar]
    return gr
#this function returns the grade of a brown scholar when a name is inputted


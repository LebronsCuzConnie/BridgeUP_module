# This document will contain all of the functions in the bridgeup module

# Add a comment at the bottom of the file explaining what your function does 
# and then add your function below

import pandas as pd

df = pd.read_csv("internship_bootcamp_data.csv")

#This function takes in a student name and returns their favorite season.

def student_season(name):
	season = df["Fav season"].loc[df["First Name"] == name]
	return season

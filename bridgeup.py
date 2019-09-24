# This document will contain all of the functions in the bridgeup module

# Add a comment at the bottom of the file explaining what your function does 
# and then add your function below

import pandas as pd

df = pd.read_csv("internship_bootcamp_data.csv")
def student_animal(name):
	student = df["First Name"]
	animal = df["Fav animal"]
	fav_animal = animal.loc[student == name]
	return fav_animal

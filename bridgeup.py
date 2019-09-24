# This document will contain all of the functions in the bridgeup module

# Add a comment at the bottom of the file explaining what your function does 
# and then add your function below

import pandas as pd

df = pd.read_csv("internship_bootcamp_data.csv")


#tells you how many people have the same fav animal as you
def animal_num(animal):
	an = df["Fav animal"]
	c = 0
	for i in an:
		if i == animal:
			c+=1
	return c


#Takes the name of student and returns their favorite ice cream flavor

def student_flavor(Name):
	Flavor = df["Fav ice cream flavor"].loc[df["First Name"] == Name]

	return Flavor


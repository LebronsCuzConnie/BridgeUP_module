# This document will contain all of the functions in the bridgeup module

# Add a comment at the bottom of the file explaining what your function does 
# and then add your function below

import pandas as pd

df = pd.read_csv("internship_bootcamp_data.csv")
def student_color(name):
	fav_color= df["Fav color"].loc[df["First Name"]== name]
	return fav_color

print(student_color("Mia"))

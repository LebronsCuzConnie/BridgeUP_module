# This document will contain all of the functions in the bridgeup module

# Add a comment at the bottom of the file explaining what your function does 
# and then add your function below

import pandas as pd

df = pd.read_csv("internship_bootcamp_data.csv")

#returns # of students that like a specific season

def season_num(season):
	number = 0
	for i in df["Fav season"]:
		if i == season:
 			number += 1
 	return number
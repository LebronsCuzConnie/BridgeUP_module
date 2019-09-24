# This document will contain all of the functions in the bridgeup module

# Add a comment at the bottom of the file explaining what your function does 
# and then add your function below

import pandas as pd

df = pd.read_csv("internship_bootcamp_data.csv")
 #It loops throught the data in the file and looks for the ice cream flavor 
 #Gives you how many people has that flavor
def flavor_num(stu_fla):
	flavor = df["Fav ice cream flavor"]
	fla_re = 0
	for i in flavor:
		if i == stu_fla:
			fla_re +=1
	return fla_re
print(flavor_num("coffee"))
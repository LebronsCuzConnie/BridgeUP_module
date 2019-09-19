
import pandas as pd 

df = pd.read_csv("internship_bootcamp_data.csv")

def student_flavor (Name):
	Flavor = df["Fav ice cream flavor"].loc[df["First Name"] == Name]

	return Flavor


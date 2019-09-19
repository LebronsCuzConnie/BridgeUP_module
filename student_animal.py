#take a student name and return their favorite animal
import pandas as pd 
df = pd.read_csv("internship_bootcamp_data.csv")
def student_animal(name):
	student = df["First Name"]
	animal = df["Fav animal"]
	fav_animal = animal.loc[student == name]
	return fav_animal

#print(student_animal("Mia"))
#print(df.head)



import pandas as pd
df = pd.read_csv("internship_bootcamp_data.csv")


#goes through the favorite color list and counts how many like a specific color
def color_num(color):
	stud_color = df["Fav color"]
	counter = 0
	for i in stud_color:
		if i == color:
			counter += 1
	return counter

#This function takes a student's name and returns their favorite color
def student_color(name):
	fav_color= df["Fav color"].loc[df["First Name"]== name]
	return fav_color

# Creates function to get Cohort from Name
def student_cohort(name):
	first_name = df["First Name"]
	cohort = df["Cohort"].loc[first_name == name] # USE BRACKETS W/ .LOC[]
	return cohort

# this function counts the amount of brown scholars in a certain grade. 
def grade_num(num): 
    grade = df["Grade"]
    total = 0 
    for i in grade: 
        if i == num: 
            total += 1 
    return total

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

<<<<<<< HEAD
df = pd.read_csv("internship_bootcamp_data.csv")

#Takes the name of student and returns their favorite ice cream flavor

def student_flavor (Name):
    Flavor = df["Fav ice cream flavor"].loc[df["First Name"] == Name]
    
    return Flavor





=======
>>>>>>> upstream/master

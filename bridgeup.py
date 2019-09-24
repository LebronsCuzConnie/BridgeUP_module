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

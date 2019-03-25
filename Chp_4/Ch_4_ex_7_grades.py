def computegrade(score):
	if score < 0.6:
		grade = "F"
	elif score >= 0.6 and score < 0.7:
		grade = "D"
	elif score >= 0.7 and score < 0.8:
		grade = "C"
	elif score >= 0.8 and score < 0.9:
		grade = "B"
	elif score >= 0.9 and score <= 1:
		grade = "A"
	return(grade)

check = False
while check == False:
	score = input("Please enter a score between 0.0 and 1.0:\n> ")
	try:
		score = float(score)
		if score < 0 or score > 1:
			print("Error: out of range, please try again\n")
			check = False
		else:
			grade = computegrade(score)
			print("Your grade is",grade)
			check = True

	except:
		print("Error: Please enter a number\n")
		check = False

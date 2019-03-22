score = input("Please enter a score between 0.0 and 0.1:\n>")
try:
	score = float(score)
	if score < 0 or score > 1:
		print("Error, out of range")
	else:
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
		print("Your grade is",grade)
except:
	print("Error: Please enter a number")

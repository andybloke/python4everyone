hours = input("Enter hours: ")
rate = input("Enter rate: ")
hours = float(hours)
rate = float(rate)
if hours > 40.0:
	extra = hours - 40
	pay = (hours - extra) * rate + extra * 1.5 * rate
	print("Pay:", pay)
else:
	pay = hours * rate
	print("Pay:", pay)
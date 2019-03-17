celsius = input("Enter the temperature in Celsius: ")
try:
	fahrenheit = float(celsius) * (9/5) + 32
	print("That is equivalent to",fahrenheit,"degrees Fahrenheit")
except:
	print("Please enter a number")
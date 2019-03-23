largest = None
smallest = None
count = 0

while True:
	number = input('Enter a number: ')
	if number == 'done':
		break
	try:
		number = float(number)
		if largest is None or number > largest:
			largest = number
		if smallest is None or number < smallest:
			smallest = number
		count = count + 1

	except:
		print('Invalid input\n')

print('Number of items entered:', count)
print('Largest number entered:', largest)
print('Smallest number entered:', smallest)
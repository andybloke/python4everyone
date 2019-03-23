count = 0
total = 0
average = 0

while True:
	number = input('Enter a number: ')
	if number == 'done':
		break
	try:
		number = float(number)
		count = count + 1
		total = total + number
	except:
		print('Invalid input')
print('Numbers entered: %d' %count)
print('Total: %d' %total)
print('Average:', total/count)
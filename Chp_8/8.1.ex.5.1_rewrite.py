# initiate empty list
total = list()

# run until break
while True: 
	number = input('Enter a number: ')
	if number == 'done': break
	try:
		number = float(number)
		total.append(number) # add to list
	except:
		print('Invalid input')
print('Numbers entered:', len(total))
print('Total:', sum(total))
print('Average:', sum(total)/len(total))
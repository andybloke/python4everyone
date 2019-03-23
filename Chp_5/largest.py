largest = None
count = 0
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
	if largest is None or itervar > largest:
		largest = itervar
	count = count + 1
	print('Loop(%d):'%count, itervar, largest)
print('\nLargest:', largest)
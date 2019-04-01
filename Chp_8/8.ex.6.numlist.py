numlist = list()
print('Enter done to finish.')
while True:
	num = input('Enter a number:')
	if num == 'done' : break
	num = float(num)
	numlist.append(num)
print('Maximum:', max(numlist))
print('Minimum:', min(numlist))
# just for fun
print('Sorted:', sorted(numlist))
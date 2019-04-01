count = 0

file = input('Enter a file name:')
fhand = open(file)
for line in fhand:
	words = line.split()
	if words == [] or words[0] != 'From' : continue
	count = count + 1
	print(words[1])

print('There were', count, 'lines in the file with From as the first word')
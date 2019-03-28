fname = input('Enter a file name:')
try:
	fhand = open(fname)
except:
	print('File not found or cannot be opened')
	exit()
for line in fhand:
	line = line.upper()
	print(line)
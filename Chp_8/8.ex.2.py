# Guardian statement
try:
	fhand = open('poo.txt')
	for line in fhand:
		words = line.split()
		# print(words) # debug line
		# if (len(words) == 0) or (words[0] != 'From'): continue
		if words == [] or words[0] != 'From': continue
		print(words[2])
except:
	print('File not found.')
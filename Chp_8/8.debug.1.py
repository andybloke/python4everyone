fhand = open('crash.txt')
for line in fhand:
	words = line.split()
	# print(words) # debug line
	# if (len(words) == 0) or (words[0] != 'From'): continue
	if len(words) <=2 or words[0] != 'From': continue
	# print(words[2]) guarded from having no 3rd element
	print(words[2])
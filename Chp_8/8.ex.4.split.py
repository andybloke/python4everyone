romeo = list()
file = input('Enter file:')
fhand = open(file)

for line in fhand:
	words = line.split()
	for word in words:
		if word in romeo: 
			continue
		else: 
			romeo.append(word.casefold()) # added to change case
			# print(romeo) # debug line

print(sorted(romeo))
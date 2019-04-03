fhand = open('words.txt')
words = dict()
count = 0

for line in fhand:
	items = line.split()
	for item in items:
		words[item] = count
		count = count + 1

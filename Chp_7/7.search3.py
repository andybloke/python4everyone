fhand = open('mbox-short.txt')
for line in fhand:
	line = line.rstrip()
	# Skip uninteresting 
	if not line.startswith('From:'):
		continue
	# Process interesting lines
	print(line)

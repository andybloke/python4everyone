count = 0
total = 0
fname = input('Enter a filename:')
try:
	fhand = open(fname)
except:
	if fname == "na na boo boo":
		print('NA NA BOO BOO TO YOU!')
		exit()
	else:
		print('File not found')
		exit()
for line in fhand:
	if line.startswith('X-DSPAM-Confidence:'):
		count = count + 1
		pos = line.find(':')
		num = float(line[pos+2:])
		total = total + num
confidence = total / count
print('Average spam confidence:', confidence)

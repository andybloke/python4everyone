import operator # added from stackexchange to sort

word = input('Enter a word:')
d = dict()
for c in word:
	if c not in d:
		d[c] = 1
	else:
		d[c] = d[c] + 1
sorted_d = sorted(d.items(), key = operator.itemgetter(1)) # sort. dont really understand it
print(sorted_d)
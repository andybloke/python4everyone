def chop(t):
	last = len(t) - 1
	del t[last]
	del t[0]
	return None

def middle(t):
	last = len(t) - 1
	t = t[1:last]
	return t

listed = list()
print('Enter \'done\' to finish.')

while True:
	item = input('Enter an item:')
	if item == 'done' : break
	listed.append(item)

newlist = middle(listed)
print('Middle:', listed)
chop(listed)
print('Chop:',listed)
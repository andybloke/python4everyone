def comesfirst(word):
	if word < 'banana':
		print('Your word, ' + word + ', comes before banana')
	elif word > 'banana':
		print('Your word, ' + word + ', comes after banana')
	else:
		print('All right, bananas.')

word = input('Enter a word: ')
word = word.casefold()
comesfirst(word)
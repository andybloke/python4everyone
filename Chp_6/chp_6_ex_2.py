def count(string, letter):
	count = 0
	for character in string:
		if character == letter:
			count = count + 1
	return count

string = input('Enter a string: ')
letter = input('Enter a letter to count: ')
count = count(string, letter)
print('The letter \"%s\" occured %d times in the string\n\"%s\" ' % (letter,count,string))
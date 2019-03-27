fruit = 'banana'
index = len(fruit) - 1
while index >= 0:
	letter = fruit[index]
	print(letter)
	index = index - 1
print('\n')
index = 0
while index > -len(fruit):
	index = index - 1
	letter = fruit[index]
	print(letter)
print('\n')
for char in fruit:
	print(char)
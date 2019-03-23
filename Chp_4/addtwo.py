def addtwo(a, b):
	added = a + b
	return added

print('Enter two numbers:')
a = int(input('>'))
b = int(input('>'))
x = addtwo(a, b)
print("\n",a,"plus",b,"=",x)
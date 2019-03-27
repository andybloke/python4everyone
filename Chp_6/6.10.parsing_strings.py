data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
print('Data:',data)
atpos = data.find('@')
print('@ at',atpos)
sppos = data.find(' ', atpos)
print('Space at',sppos)
host = data[atpos+1:sppos]
print('Host:',host)

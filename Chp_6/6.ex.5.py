string = 'X-DSPAM-Confidence:0.8475'
print(string)
position = string.find(':')
num = float(string[position+1:])
print(num)
print(type(num))
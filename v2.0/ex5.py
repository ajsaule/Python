#find position of colon character
str = 'X-DSPAM-Confidence:0.8475'
pos = str.find(':')
print(pos)
#find position of end of floating point
pos2 = str.find('5',pos)
print(pos2)
#print the desired section of string
string = str[pos+1:pos2]
print(string)
#convert section into float
fstring =float(string)
print(fstring)

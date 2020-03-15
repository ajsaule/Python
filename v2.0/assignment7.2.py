#Use filename mbox-short.txt
add = 0
count = 0
file = input('Enter a filename: ')
file1 = open(file)
for line in file1:
    if line.startswith('X-DSPAM-Confidence:'):
        #review the slicing and how to assign values there Assignment 7.2
        line1 = float(line[20:26])
        add = add + line1
        print(add)
        #^ TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'float'
        count = count + 1
        # I dont really understand how this gives a count ..
print('Average spam confidence:', add/count)


# Use the file name mbox-short.txt as the file name
#add = 0
#count = 0
#file = input('Enter a filename: ')
#file1 = open(file)
#for line in file1:
#    if line.startswith('X-DSPAM-Confidence:'):
#        line1 = float(line[20:26])
#        add = add + line1
#        count = count + 1
#print('Average spam confidence:', add/count)

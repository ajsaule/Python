#Use filename mbox-short.txt
try:
    file = input('Enter a filename: ')
if file = 'gimp':
    print = ('You wanna go m8?!?')
except:
    print = ('Enter a valid filename please?')
file1 = open(file)s
for line in file1:
    if line.startswith('X-DSPAM-Confidence:'):
        line1 = float(line[20:26])
        add = add + line1
        # ^ TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'float'
        count = line1 + 1
        # I dont really understand how this gives a count ..
print('Average spam confidence:', add/count)

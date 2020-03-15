file = input('Enter a filename: ')
file1 = open(file)
for line in file1:
    if line.startswith('X-DSPAM-Confidence:'):
        line1 = float(line[20:26])
        sum = sum + line1
        # ^ TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'float'
        count = line1 + 1
        # I dont really understand how this gives a count ..
print('Average spam confidence:', sum/count)

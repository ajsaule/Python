file = open(input('Please type filename to open: '))
read = file.read()
count = dict()
for line in read:
    if line.startswith('From'):
        select = dict(str(line[34:36]))
        print(count)

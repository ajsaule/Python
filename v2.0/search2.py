while True:
	try:
		file = input('Please enter the desired filename: ')
		filen = open(file)
	except:
		print('Enter a vailid filename please!')
		continue
	count = 0
	for line in filen:
		if line.startswith('Subject:'):
			count = count + 1
	print ('There were', count, 'subject lines in', file)
	exit ()

largest = None
smallest = None
while True:
	try:
		num = input('Enter a number: ')
		if num == 'done' :
			break
		nu = float(num)
        elif nu > largest :
            largest = nu
        elif nu < smallest :
            smallest = nu
    except:
    	print ('Invalid input')
print ('Maximum is', largest)
print ('Minimum is', smallest)

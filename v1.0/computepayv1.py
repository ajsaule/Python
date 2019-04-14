def computepay() :
	if h > 40:
		grosspay = (h-40) * r * 1.5
		gpay = grosspay + (40*r)
		return gpay
	else:
		payg = (h*r)
		return payg
h = float(input('Enter Hours: '))
r = float(input('Enter Pay rate: '))
computepay()
print (gpay)

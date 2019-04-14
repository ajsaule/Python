hours = input('Enter hours worked: ')
rate = input('Enter rate of pay: ')
#
try:
    hrs = float(hours)
    ratE = float(rate)
    if hrs > 40 :
        grosspay = hrs * (ratE + 1.5)
        print (grosspay)
except:
    print ('Please enter numeric values')
else :
    grosspaY = (hrs * ratE)
    print (grosspaY)

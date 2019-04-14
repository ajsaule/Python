def computepay ():
    Hrs = input('Total hours worked: ')
    Rate = input('Rate of pay: ')
computepay ()
hrs = float(Hrs)
rate = float(Rate)
if Hrs > 40:
    grosspay = (hrs-40) * rate * 1.5
    gpay = grosspay + (40 * rate)
    print (gpay)
else:
    Grosspay = (hrs * rate)
    print (Grosspay)

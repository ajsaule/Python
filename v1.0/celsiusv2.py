#inp = input('Enter degrees in Fahrenheit: ')
#Far = float(inp)
#cel = (far - 32.0) * 5.0 / 9.0
#print (cel)

#The above will fail if someone enters nonsensical string into the input.
#We can use the try: or except: functions to catch errors and prompt the user to re-enter text.

inp = input('Enter degrees in Fahrenheit: ')
try:
  far = float(inp)
  cel = (far - 32.0) * 5.0 / 9.0
  print(cel)
except:
  print('Please enter a valid number')

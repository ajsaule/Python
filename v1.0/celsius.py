celsius = input('What is the temperature right now - ')
cel = int(celsius)
#why does it throw: IndentationError: unexpected indent
if cel > 50:
    print ('Evacuate!! Meltdown imminent')
print ('Let me use magic to convert that to Fahrenheit')
far = cel * 1.8
print (far)

file = open('mbox.txt')
for line in file:
	# Need to have .linestrip before the if statement to isolate find.
	line = line.strip()
	if line.find('@uct.ac.za') == -1:
		continue
	print(line)

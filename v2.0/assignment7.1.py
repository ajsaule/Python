# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fhl = fh.read()
fhli = fhl.upper()
fhlin = fhli.rstrip()
print(fhli)

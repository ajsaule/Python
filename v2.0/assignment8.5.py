#Inputting filename for sorting 
fname = input("Enter file name: ")
#Below is just a buffer allowing to enter no text and by default open 'mbox-short.txt'
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
#Set count at 0 for summing total number of times From appears
count = 0
#Function, allows us to convert string or, list into a single element
def convert(line):
    s = [str(i) for i in line] #Not sure how this works exactly
    res = str("".join(s))
    return(res)
#For the lines in opened file, select lines starting with 'From_'
for line in fh:
    if line.startswith('From '):
        #Counting the number of lines it appears in
        count = count + 1
        #Turning this data into a list
        emails = line.split()
        #Splitting and selecting the first position after 0 in the list
        email = emails[1:2]
        #Call our convert function and execute on email list, turining the arguments into single elements
        print(convert(email))
        #Print the text and count for all the data shown
print("There were", count, "lines in the file with From as the first word")

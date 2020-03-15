#Open file and read through
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
#Loop through first iteration and strip /n tags, split spaces into a list
for line in fh:
    line = line.rstrip()
    words = line.split()
    #Nested loop to iterate and add each word only once, no duplicates
    for line in words:
        if line not in lst:
            lst.append(line)
            #Finally sort ascending order
            lst.sort()
#Print final list 
print(lst)

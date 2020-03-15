#Code bewlo removes both first and last, returning None
#list = ['one', 'two']
#list1 = list.remove('one')
#list2 = list.remove('two')
#print (list1)

#Defined function removes middle argument
list = ['first','second','third']
def middle(second):
    del second[1]
middle(list)
print(list)

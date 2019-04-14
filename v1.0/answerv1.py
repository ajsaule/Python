count = 0
sum = 0
#Looping statement at beginning
while True:
    #try, except statement to stop anything other than numeric values
    try:
        answer = input('Enter number > ')
        if answer == 'done' :
            break
        #Convert default string to float for calculations
        ans = float(answer)
        print('Your number', ans)
        #Calculations for count, sum, average
        sum = sum + ans
        count = ans + 1
    except:
        print ('Enter only numeric values plz   ')
#Final prints for ouput of data
print('Done!')
print(sum, count, sum/count)

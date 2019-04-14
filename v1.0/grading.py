print ('Welcome to your friendly grading system')
grad = input('Please input your recent test result: ')
try:
    if grad >= 0.9 :
        print ('A')
    elif grad >= 0.8 :
        print ('B')
    elif grad >= 0.7 :
        print ('C')
    elif grad >= 0.6 :
        print ('D')
    else grad < 0.6 :
        print ('F. Sorry you have to re-take the test')
except:
    print ('Please enter a numeric value between 0 and 0.99')

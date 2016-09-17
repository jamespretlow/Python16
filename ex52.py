'''
 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers.
 If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
 Enter the numbers from the book for problem 5.1 and Match the desired output as shown
 '''
#enter a number convert it into a foalting point and read it

count = 0
total = 0
while True:
    iput = raw_input('Enter Number')
    
    #Handle edge cases
    if iput == 'done' : break
    if len(iput) < 1 : break
    
    #Do the work
    try :
        num = float(iput)
    except:
        print 'Invalid'
        continue
        
    count = count + 1
    total = total + num
    print num, total, count
    

print 'Average = ', (total / count)
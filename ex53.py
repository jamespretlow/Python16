large = None
small = None

while True:
    iput = raw_input("Enter a number: ")
    if iput == "done" : break
    try:
        num = float(iput)
    except:
       # print "Please enter a number as input or \'done\'"
        print "Invalid input"
        continue
    if small is None:
        small = num 
    if num > large :
        large = num
    elif num < small :
        small = num

def done(large,small):
    print "Maximum is", int(large)  
    print "Minimum is", int(small)

done(large,small)

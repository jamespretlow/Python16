hrs = raw_input ('What are your hours?')
rte = raw_input ('What is your rate?')

hours = float(hrs)
rate = float(rte)

if hrs > 40:
    s_h = hours
    o_h = hours - 40
    straight_hours = float(s_h)
    overtime_hours = float(o_h)
    pay = (straight_hours * rate) + (overtime_hours * (rate *1.5))
    print "Your pay is ", "$",pay,   

if hrs <= 40:
    pay = hours * rate
    print pay
    
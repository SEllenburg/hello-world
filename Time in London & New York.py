import datetime
now1 = datetime.datetime.now() + datetime.timedelta(hours=3)
now2 = datetime.datetime.now() + datetime.timedelta(hours=8)
print "Current date and time in New York:"
print str(now1)
print "Current date and time in London:"
print str(now2)
if now1.hour < 9 or now1.hour > 20:  
    print "The New York City Branch is Closed"
else:
    print "The New York City Branch is Open"
if now2.hour < 9 or now2.hour > 20:  
    print "The London Branch is Closed"
else:
    print "The London Branch is Open"

##print
##
##print "Current date and time using str method of datetime object:"
##print str(now)
##
##print
##print "Current date and time using instance attributes:"
##print "Current year: %d" % now.year
##print "Current month: %d" % now.month
##print "Current day: %d" % now.day
##print "Current hour: %d" % now.hour
##print "Current minute: %d" % now.minute
##print "Current second: %d" % now.second
##print "Current microsecond: %d" % now.microsecond
##
##print
##print "Current date and time using strftime:"
##print now.strftime("%Y-%m-%d %H:%M")
##
##print
##print "Current date and time using isoformat:"
##print now.isoformat()


import time
#epoch means : when your computer thinks time began (reference point)


#print(time.ctime(0)) // returns epoch in date 
#print(time.time()) // current time in epoch in seconds

#print(time.ctime(time.time())) // return the date of the day

#time.localtime() # returns time object based on the current time 

#time_obj = time.localtime()
#print(time_obj) # to convert this time obj to a readable str 
                # we'll need the help of the separate fct strftime
#current_time = time.strftime("%d %B %Y %H:%M:%S",time_obj)
#print(current_time)

timestr="20 April, 2020"

time_object = time.strptime(timestr, "%d %B, %Y")

print(time_object)


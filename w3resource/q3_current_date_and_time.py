import datetime                             #import date and time module
now = datetime.datetime.now()               #storing the current date and time in variable
print("Current Date and Time:")
print(now.strftime("%Y-%m-%d\t%H:%M:%S"))   #Accessing the date and time as string

#In date only Year in Caps
#In time all were Caps
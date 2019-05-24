# intialising a String
a = 'GeeksforGeeks'
print(a)

#initialising a byte object
c = b'GeeksforGeeks'
print(c)
#using encode() to encode the String
#encoded version of a is stored in d
#using ASCII mapping
d = a.encode('ASCII') #try 'utf-16' or 'utf-8'(ASCII)
print(d)

#checking if a is converted to bytes or not
if(d==c): print("Encoding successful")
else: print("What the hell is this?")
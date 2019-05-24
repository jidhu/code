
# Python code to demonstrate naive
# method to compute gcd ( recursion )

def gcd(a,b):
    if a == b:
        return a
    else:
        if a > b:
            return gcd(a-b,b)
        else:
            return gcd(a,b-a)
a = 96
b= 48

print ("The gcd of 60 and 48 is : ",end="")
print (gcd(a,b))


'''
def computeGCD(x, y):

   while(y):
       x, y = y, x % y

   return x

a = 60
b= 48

# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(60,48))

'''
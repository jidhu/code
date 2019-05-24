#Soln 1
from math import log

x = int(input("Enter the number?\n> "))
count = 0
while(x!=0):
    count+=1
    x//=10
  #  print(x)
print(count)


#Soln 2
x = int(input("\nEnter the number?\n> "))
print(int(log(x,10)+1))
input()
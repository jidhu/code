a = input("enter the string\n> ")
n = len(a)
count=(1<<n)                    #instead of 2**n

for i in range(0,count):        #traverse through every line
    for j in range(0,n):        #traverse through every bit
        if (i & (1<<j))>0:
            print(a[j],end = ' ')
    print('')
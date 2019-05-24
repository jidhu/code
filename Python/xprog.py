a = input("Enter the name\n> ")
if ((len(a)&1)!=0):
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            if (i==j or i+j==(len(a)-1)):
                print(a[i],end='')
            else:
                print(" ",end='')
        print("\n")


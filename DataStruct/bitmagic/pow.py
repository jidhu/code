x = int(input("Enter the value\n> "))
if (x and not(x&(x-1))):
    print("Yes, It's the power")
else:
    print("Nope")
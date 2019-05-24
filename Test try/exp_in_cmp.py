# Lesson of this code: ANYTHING TO THE POWER OF ZERO (that anything includes zero)

a = 0
b = a ** 0
if b < a + 1:
    c = 1
    print("1st condition is True")
elif b == 1:
    c = 2
    print("2nd condition is True")
else:
    print("Your life turns out")
    c = 3
print(a, b, c)
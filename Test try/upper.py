# upper function CAPITALIZE but you need to save it in a variable

a = []
s = 'python'
for i in range(len(s)):
    i = s[i].upper()
    a.append(i)
print(s, end="\n")
print(a.join())
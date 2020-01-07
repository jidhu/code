n = 10
s = "abcac"
len = len(s)

comsstr = n // len
remsstr = n % len
count = 0
for i in s:
    if s[i] == 'a':
        count+=1

print(count*comsstr+remsstr)

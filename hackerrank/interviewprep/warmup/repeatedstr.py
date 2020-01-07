n = 10
s = "abcac"
len = len(s)

comsstr = n // len
remsstr = n % len
count = 0
for i in range(len):
    if s[i] == 'a':
        count+=1
    if s[i] == 'a' and i < remsstr:
        rmcount+=1

print(count*comsstr+rmcount)

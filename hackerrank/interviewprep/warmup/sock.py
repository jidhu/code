n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
har = [0]*n
count,pair = 0,0

for i in range(n):
    if har[i] == 0:
        count = 0
        har[i] = 1
        for j in range(i+1,n):
            if ar[i] == ar[j]:
                har[j]=1
                count+=1
        pair += (count+1)//2
print(pair) 

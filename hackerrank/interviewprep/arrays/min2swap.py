arr = [2, 3, 4, 1, 5]
n = len(arr)
sarr = [i+1 for i in range(n)]

i,j,swap=0,0,0
while(j<n):
    i = j+1
    while(i<n):
        if arr[i]!=carr[i] and (arr[i] == sarr[j]):
            arr[i],arr[j] = arr[j],arr[i]
            swap+=1
            break
        i+=1
    j+=1
print(swap)

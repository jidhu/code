n = 8
arr = [1, 2, 5, 3, 7, 8, 6, 4]
chaos = 0

i,j=0,0
while i<n:
    chaos = i+1 - arr[i]
    if chaos > 2:
        print("too")
        break
    if chaos <= 0:
        i+=1
        continue
    j += chaos
    i+=1
print(j)

n = 5
arr = [2, 1, 5, 3, 4]
carr = [i+1 for i in range(n)]
chaos = 0

i,j = 0,0
while i < n:
    if carr[j] == arr[i]:
        i+=1
        j+=1
        continue
    if i+1 < n:
        if carr[j] == arr[i+1]:
            chaos += 1
            i+=2
            j+=1
            continue
    if i+2 < n:
        if carr[j] == arr[i+2]:
            chaos += 2
            i+=3
            j+=1
            continue

    movement = chaos
    chaos = 0
    i+=1

print(movement)

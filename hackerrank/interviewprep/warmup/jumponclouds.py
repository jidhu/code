n = 7
c = [0, 1, 0, 0, 0, 1, 0]
steps,i = 0,0
while (i<n):
    if c[i] == 0:
        if i+2 < n:
            if c[i+2] == 0:
                steps += 1
                i += 2
                continue
        if i+1 < n:
            if c[i+1] == 0:
                steps += 1
    i+=1
print(steps)

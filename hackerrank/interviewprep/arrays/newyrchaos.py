arr = [1, 2, 5, 3, 7, 8, 6, 4]
n = len(arr)
chaos = 0

def swap(a,b):
    temp = a
    a = b
    b = temp

i=n-1
while(i>=0):
    if (i+1) != arr[i]:
        if (i-1) >= 0 and i+1 == arr[i-1]:
                chaos += 1
                arr[i],arr[i-1] = arr[i-1],arr[i]

        elif (i-2) >= 0 and i+1 == arr[i-2]:
                chaos += 2

                arr[i-2],arr[i-1] = arr[i-1],arr[i-2]
                arr[i-1],arr[i] = arr[i],arr[i-1]

        else:
            print('Too chaotic')
            break

    i-=1
print(chaos)

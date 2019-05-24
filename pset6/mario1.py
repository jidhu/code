height = int(input("Height: "))
space = height - 1
#rspace = height -1
ash = 1
#rash = 1
i=0
if(height>0 and height < 23):
    while(i<height):
        for j in range(0,space):
            print(" ",end='')
        for k in range(0,ash):
            print('#',end='')
        print('  ',end='')
        for k in range(0,ash):
            print('#',end='')
        for j in range(0,space):
            print(" ",end='')
        i+=1
        space -= 1
        ash += 1
        print('\n',end='')
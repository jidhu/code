height=int(input('Height: '))
space=height - 1
ash=2
i = 0
if(height > 0 and height < 180):
    while(i < height):
        for j in range(0,space):

            print(' ',end='')
        for k in range(0,ash):
            print("#",end='')
        i+=1
        space -= 1
        ash += 1
        print('\n',end='')
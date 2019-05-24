T = int(input())
while T>0:
    x = int(input())
    if x == 0:
        print(0)
    else:
        for i in range(1,32):
            if x&(1<<(i-1))!=0:
                print(i)
                break
    T-=1
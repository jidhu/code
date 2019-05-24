T = int(input())
while T>0:
    N = int(input())
    K = int(input())
    K+=1
    if (N&(1<<(K-1)))!=0:
        print('Yes')
    else:
        print("No")
    T-=1
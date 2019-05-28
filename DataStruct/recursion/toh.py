def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

T=int(input())
while(T>0):
    n=int(input())
    a = "First Rod"
    b = "Second Rod"
    c = "Third Rod"
    TowerOfHanoi(n, a, c, b)
    T-=1
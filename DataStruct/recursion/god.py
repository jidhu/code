def rec(n,k):
    if n==1:
        return n
    return (rec(n-1,k)+ k - 1 )% n+1

n = 5
k = 2
print(rec(n,k))

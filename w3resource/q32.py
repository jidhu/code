def gcd(a, b):
    if a == b:
        return a
    else:
        if a > b:
            return gcd(a-b, b)
        else:
            return gcd(a, b-a)

def lcm(a, b):
    return a*b/gcd(a, b)

a = 5
b = 10
print(int(lcm(a, b)))
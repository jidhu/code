def add(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Vijay please enter a integer value!")
    return (a+b)

print(add(23.4, 10))
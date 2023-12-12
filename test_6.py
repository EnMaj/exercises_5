def degree5n_2(n,degree,a):
    if n == a:
        return degree
    elif a > n:
        return -1
    return degree5n_2(n,degree +1,a*5)

def degree5n(n):
    degree = 1
    a=5
    return degree5n_2(n,degree,a)

print(degree5n(25))
def degree5n(n):
    degree = 0
    if n%5 ==0:
        degree+=1
        n //=5
        degree += degree5(n)
    
    elif degree == 0 and n!=1:
        return -1
    return degree

print(degree5n(25))

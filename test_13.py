def odd_list(a,n):
    if n==0:
        return a
    y = a.pop(0)
    if y%2 == 0:
        a.append(y)
    return odd_list(a,n-1)


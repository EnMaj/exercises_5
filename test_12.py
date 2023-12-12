def search(a,x):
    if len(a) == 0:
        return 0
    elif a[-1] == x:
        return 1
    a.pop()
    return search(a,x)

a = [7,2,4,4,0,6]
print(search(a,4))
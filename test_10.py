def maxlist(a):
    if len(a) == 1:
        return a[0]
    else:
        if a[0]>a[-1]:
            a.pop()
            return maxlist(a)
        a[0] = a[-1]
        a.pop()
        return maxlist(a)

a = [1,2,7,4,7,6]
print(maxlist(a))
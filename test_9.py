def combin(n,k):
    if k==n or k==0:
        return 1
    return combin(n-1,k) + combin(n-1,k-1)

print(combin(10,5))
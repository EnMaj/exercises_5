def ind_maxlist(a):
    if a[-1] == max(a):
        return len(a)-1
    a.pop()
    return ind_maxlist(a)


a = [7,2,4,4,0,6]
print(ind_maxlist(a))

def sum_progress(a1,r,n):
    if n!=1:
        a_i = a1 + r
        return a1 + sum_progress(a_i,r,n-1)
    return a1


print(sum_progress(2,3,4))
def simmetr(s,i,j):
    if s[i]!=s[j] or (j-i+1)%2!=0:
        return False
    elif (i-j)==1:
        return True
    else:
        return simmetr(s,i+1,j-1)

print(simmetr("abcaba",0,5))

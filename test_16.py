def ten_to_n(x,n):
    str_letters = "0123456789ABCDEF"
    if x == 0:
        return ""
    return ten_to_n(x//n,n) + str_letters[x%n]

print(ten_to_n(1020,16))

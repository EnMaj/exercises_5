


a = "1234"
b = "5612378"
max_len = 0
for i in range(len(a)):
    for j in range(len(a)-i):
        if a[j:j+i] in b:
            max_len = i
print(max_len)


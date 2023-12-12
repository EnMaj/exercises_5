def fib(k):
    if k == 1 or k ==2:
        return 1
    return fib(k-1) + fib(k-2)

print(fib(6))
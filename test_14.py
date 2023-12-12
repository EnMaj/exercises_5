def numbers(x):
    if x>0:
        print(x%10)
        numbers(x//10)

numbers(1234)
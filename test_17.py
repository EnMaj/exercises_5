def function2(x,divider):
    if divider > int(x**0.5):
        return 1
    elif x%divider == 0:
        return 0
    return function2(x,divider+1)

def function1(x):
    divider = 2
    return function2(x,divider)

print(function1(150))
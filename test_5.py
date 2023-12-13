def mod_number(a,b):
    if a >= b:
        return mod_number(a-b,b)
    else:
        return a

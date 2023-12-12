def count(a,b):
    if b == a:
        return 1
    else:
        b = b-a
        return 1 + count(min(b,a),max(b,a))

print(count(5,6))
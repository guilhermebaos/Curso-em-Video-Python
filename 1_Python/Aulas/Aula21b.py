def fatorial(n):
    f = 1
    for c1 in range(n, 0, -1):
        f *= c1
    return f


print(fatorial(4))
print(fatorial(5))

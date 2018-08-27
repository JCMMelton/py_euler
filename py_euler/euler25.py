a, b, n = 1, 1, 2
while len(str(a)) != 1000:
    a, b, n = a+b, a, n+1
print(n)



def e(n):
    return n/2

def o(n):
    return 3*n + 1

def collatz(n):
    c = 0
    while n != 1:
        if n%2==0:
            n = e(n)
        else:
            n = o(n)
        c += 1
    return c

m = 0
a = 0
for i in range(2, 1000001):
    c = collatz(i)
    if c > m:
        m = c
        a = i

print a

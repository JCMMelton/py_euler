import sets

def d(n):
    a = 0
    for i in range(1, n):
        if n % i == 0:
            a += i
    return a

abunds = []

limit = 28123

ans = [1,2,3,4,5,6,7,8,9,10,11]

for n in range(1, limit):
    if d(n) > n:
        abunds.append(n)

print(len(abunds))

abundsums = set([])
for a in abunds:
    for b in abunds:
        x  = a + b
        if x < limit:
            abundsums.add(x)

print(len(abundsums))

ans = 0
for x in range(0, limit):
    if x not in abundsums:
        ans += x

print(ans)

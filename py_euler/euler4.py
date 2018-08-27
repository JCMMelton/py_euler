a = 1000

def is_pal(n):
    s = str(n)
    for i in range(0, int(len(s)/2)):
        if s[i] != s[::-1][i]:
            return False
    return True

pals = []
while a > 99:
    for e in range(999, 99, -1):
        if is_pal(a*e):
            pals.append(a*e)
    a -= 1

m = 0
for p in pals:
    if p > m:
        m = p

print(m)

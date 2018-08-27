n = m = 20

def cool(n, m):
    for i in range(2,m+1):
        if not n%i == 0:
            return False
    return True


while not cool(n,m):
    n+=m

print(n)

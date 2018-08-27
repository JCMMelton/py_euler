facti = 600851475143

limit = 10000
primes = [2,3,5]
n = 6

def is_prime(n, primes):
    for p in primes:
        if ((n/p)%1 == 0):
            return False
    return True

while n < limit:
    if is_prime(n, primes):
        primes.append(n)
    n += 1

for p in reversed(primes):
    if facti%p == 0:
        print(p)
        break

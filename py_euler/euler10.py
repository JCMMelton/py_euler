primes = [2,3,5]
n = 6

def is_prime(n, primes):
    for p in primes:
        if n%p == 0:
            return False
    return True

while n < 2000000:
    if is_prime(n, primes):
        primes.append(n)
    n += 1

print sum(primes)

def is_prime(n, primes):
    for p in primes:
        if n%p == 0:
            return False
    return True

primes = [2,3,5]
n = 6
limit = 10001

while True:
    if len(primes) == limit:
        break
    if is_prime(n, primes):
        primes.append(n)
    n += 1

print(primes[-1])

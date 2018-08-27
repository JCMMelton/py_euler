import math
import time

current_triangle = 1
n = 1

prime_limit = 10**5
primes = [2,3,5]
prime = 6

def is_prime(n, primes):
    for p in primes:
        if n%p == 0:
            return False
    return True

def is_sqr_of_prime(n, primes):
    for p in primes:
        if n**2 == p:
            return True
    return False

def count_div(tri, primes):
    return count_div_med(tri)
    # return count_div_slow(tri)
    # return count_div_prime(tri, primes)

def count_div_prime(tri, primes):
    print "\n\n"
    ans = 1
    for p in primes:
        print "testing prime " + str(p) + " on " + str(tri)
        if p*p*p > tri:
            print str(p*p*p) + " > " + str(tri)
            break
        count = 1
        print "while tri divisible by "+ str(p)
        while tri % p == 0:
            tri = tri/p
            count += 1
            print str(tri) + " count + 1"
        ans = ans * count
    if is_prime(tri, primes):
        print "tri is prime"
        ans = ans * 2
    elif is_sqr_of_prime(tri, primes):
        print "tri is sqare of prime"
        ans = ans * 3
    elif tri != 1:
        print str(tri) + " not equal to 1"
        ans = ans * 4
    return ans

def count_div_slow(tri):
    # factors = [1]
    count = 2
    limit = (tri/2 if tri%2==0 else (tri+1)/2)+1
    # print "tri " + str(tri) + " limit " + str(limit)
    for i in range(2, limit):
        if tri%i == 0:
            # factors.append(i)
            count += 1
    # factors.append(tri)
    # print "factors from slow"
    # print factors
    return count


def count_div_med(tri):
    # factors = [1]
    count = 1
    for i in range(2, int(math.ceil(math.sqrt(tri)))):
        if tri%i == 0:
            count += 1
            # factors.append(i)
        elif i != n/i:
            count += 1
            # factors.append(i)
    # factors.append(tri)
    # print "factors from med"
    # print factors
    return count


# test_num = 13410934
# run_limit = 1000
# start_med = time.time()
# run_count = 0
# while run_count < run_limit:
#     count_div_med(test_num)
#     run_count+=1
# end_med = time.time()
# run_time_med = end_med - start_med
#
# start_slo = time.time()
# run_count = 0
# while run_count < run_limit:
#     count_div_slow(test_num)
#     run_count+=1
# end_slo = time.time()
# run_time_slo = end_slo - start_slo
#
# print "run time med was "+ str(run_time_med)
# print "run time slo was "+ str(run_time_slo)

#build list of primes up to prime_limit
# while prime < prime_limit:
#     if is_prime(prime, primes):
#         primes.append(prime)
#     prime += 1
# print "Done building primes"

while True:
    # cmed = count = count_div(current_triangle, primes)
        # cmed = count_div_med(current_triangle)
    count = cslo = count_div_slow(current_triangle)
    # print count
    # print 'n: ' + str(n) + ' tri: ' + str(current_triangle) + ' count_med: ' + str(cmed) + ' count_slo: ' + str(cslo)
    # print "\n"
    if count >= 500:# or n > 10:
        print str(current_triangle)
        print str(count)
        break
    n += 1
    current_triangle += n

# print count_div(5000)

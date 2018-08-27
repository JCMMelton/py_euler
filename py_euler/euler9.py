# euler 9
import math

prompt = '''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
(1000-b-c)^2 + b^2 = c^2
(1000-b-c)^2 = c^2 - b^2

a^2 + b^2 = 1000-b-a

'''

pythags = []

for a in range(1, 999):
    for b in range(a, 999):
        a2 = a**2
        b2 = b**2
        c2 = a2 + b2
        c  = math.sqrt(c2)
        if a < b and b < c and c%1==0 and a+b+c == 1000:
            pythags.append([a, a2, b, b2, c, c2, a+b+c])

for p in pythags:
    print p

print str(p[0]) + ' ' + str(p[2]) + ' ' + str(p[4])
print p[0] * p[2] * p[4]

from decimal import *

getcontext().prec = 1000

for i in range(2, 8):
    # print Decimal(1) / Decimal(i)
    # print Decimal(1.0/i)
    dec = Decimal(1) / Decimal(i)
    print(i, dec)
    # for d in str(dec):
    #     print(d)
print(getcontext())

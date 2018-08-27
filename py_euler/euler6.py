sqrs = [x*x for x in range(1,101)]
print(sqrs)
sums = sum([x for x in range(1,101)])
print(sums)

print(sums*sums - sum(sqrs))

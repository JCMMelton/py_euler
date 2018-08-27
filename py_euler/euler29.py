limit = 100
limit += 1
powers = []
for a in range(2, limit):
    for b in range(2, limit):
        powers.append(a**b)

powers = list(set(powers))
powers.sort()
# print(powers)
print(len(powers))

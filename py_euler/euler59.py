import itertools
import re
from string import ascii_lowercase

def file_to_bin():
    with open('p059_cipher.txt') as en_file_raw:
        en_file = [line for line in en_file_raw]
        bins = [int(line) for line in en_file[0][0:-1].split(',')]
    return bins

def decr(bins, letters):
    k = []
    for b in range(0,len(bins)):
        print(bins[b], letters[b%3], ord(letters[b%3]), bins[b] ^ ord(letters[b%3]), chr( bins[b] ^ ord(letters[b%3]) ))
        k.append( chr( bins[b] ^ ord(letters[b%3]) ) )
    r = "".join(k)
    if re.search(" the ", r) != None:
        print("\n")
        print(r)
        print(letters)
    return r

def solve(bins, letters):
    s = 0
    for b in range(0,len(bins)):
        d = bins[b] ^ ord(letters[b%3])
        s += d
    return s

# print(file_to_bin())
l = ascii_lowercase
bins = file_to_bin()

# x = 0
# for a in range(0, 26):
#     for b in range(0, 26):
#         for c in range(0, 26):
#             # x+=1
#             # print(x)
#             decr(bins, [l[a], l[b], l[c]])

decr(bins, ['g','o','d'])
solution = solve(bins, ['g','o','d'])
print(solution)

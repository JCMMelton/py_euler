# f the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

single_digit_words = [
'one',
'two',
'three',
'four',
'five',
'six',
'seven',
'eight',
'nine'
]
teen_deigit_words = [
'ten',
'eleven',
'twelve',
'thirteen',
'fourteen',
'fifteen',
'sixteen',
'seventeen',
'eighteen',
'nineteen'
]

tens_digit_words = [
'twenty',
'thirty',
'forty',
'fifty',
'sixty',
'seventy',
'eighty',
'ninety'
]
hundred = 'hundred'
thousand = 'thousand'

total = 0
c = 0
for x in [len(s) for s in single_digit_words]:
    total += x
    c+=1
print(total)
for x in [len(s) for s in teen_deigit_words]:
    total += x
    c+=1
print(total)

for tens in tens_digit_words:
    total += len(tens)
    c+=1
    for s in single_digit_words:
        # print(tens + s)
        total += len(tens) + len(s)
        c+=1
        # print(c)
print(total)
one_to_nn = total
print(c)
for s in single_digit_words:
    total +=  len(s) + len(hundred)
    total += ((len(s) + len(hundred) + len('and'))*99) + one_to_nn
    # print(s + ' ' + hundred)
    # for tens in tens_digit_words:
        # for si in single_digit_words:
            # print(s + ' ' + hundred + ' and ' + tens + ' ' + si)

# print(total)

print(total)
print(total + len('one') + len(thousand))
# for i in range(100, 1):

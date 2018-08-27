import time

#                             75
#                           95  64
#                         17  47  82
#                       18  35  87  10
#                     20  04  82  47  65
#                   19  01  23  75  03  34
#                 88  02  77  73  07  63  67
#               99  65  04  28  06  16  70  92
#             41  41  26  56  83  40  80  70  33
#           41  48  72  33  47  32  37  16  94  29
#         53  71  44  65  25  43  91  52  97  51  14
#       70  11  33  28  77  73  17  78  39  68  17  57
#     91  71  52  38  17  14  91  43  58  50  27  29  48
#   63  66  04  68  89  53  67  30  73  16  69  87  40  31
# 04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

numsf = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

#     3
#    7 4
#   2 4 6
#  8 5 9 3
# 2 5 8 3 5

#     3
#    7 4     [10, 7]
#   2 4 6    [12, 14, 11, 10]
#  8 5 9 3   [20]
# 2 5 8 3 5

nums = '''
3
7 4
2 4 6
8 5 9 3
'''

# 2 5 8 3 5





class Node():
    n = 0
    a = 0
    b = 0
    vals = []
    index = 0
    row = 0
    ego = 0


    def __init__(self, n, index, row, ego):
        self.n = n
        self.a = n
        self.index = index
        self.row = row
        self.ego = ego
        self.vals = []

    def vals_to_str(self):
        return ' '.join([str(v) for v in self.vals])

    def add(self, adder):
        self.vals.append(self.n + adder)

    def test(self):
        print("node " +str(self.ego) + " index " + str(self.index) + " row " + str(self.row) + " number " + str(self.n) + " values " + self.vals_to_str() )


numbers_raw = numsf.split('\n')

numbers = []
for n in numbers_raw:
    if n == '':
        continue
    numbers.append([int(i) for i in n.split(' ')])

def cycle_over_nodes(nodes, callback):
    for n1 in range(0, len(nodes)-1):
        for n2 in range(0, len(nodes[n1])):
            callback()

def build_nodes(numbers):
    nodes = []
    ego = 0
    for r in range(0, len(numbers)):
        node_row = []
        nrow = numbers[r]
        for n in range(0, len(nrow)):
            node_row.append(Node(nrow[n], n, r, ego))
            ego += 1
        nodes.append(node_row)
    return nodes

def brute(numbers):
    nodes = build_nodes(numbers)
    nodes[0][0].add(0)

    for n1 in range(0, len(nodes)-1):
        for n2 in range(0, len(nodes[n1])):
            for v in nodes[n1][n2].vals:
                nodes[n1+1][n2].add(v)
                nodes[n1+1][n2+1].add(v)

    final_vals = []
    for node in nodes[-1]:
        final_vals += node.vals
    return max(final_vals)

def heat(numbers):
    nodes = build_nodes(numbers)
    ans = 0
    for n1 in range(len(nodes)-2, 0, -1):
        for n2 in range(0, len(nodes[n1])):
            if nodes[n1+1][n2].a > nodes[n1+1][n2+1].a:
                nodes[n1][n2].a += nodes[n1+1][n2].a
            else:
                nodes[n1][n2].a += nodes[n1+1][n2+1].a
    if nodes[1][0].a > nodes[1][1].a:
        ans = nodes[0][0].a + nodes[1][0].a
    else:
        ans = nodes[0][0].a + nodes[1][1].a
    return ans

print("----------\n")
brute_start = time.time()
final_ans_brute = brute(numbers)
brute_end = time.time()
brute_elapsed = brute_end - brute_start
print("Brute took " + str(brute_elapsed) + " time units")

print("\n")

heat_start = time.time()
final_ans_heat = heat(numbers)
heat_end = time.time()
heat_elapsed = heat_end - heat_start
print("Heat took " + str(heat_elapsed) + " time units")

print("::\n")
# print max(final_vals)
correct_ans = 1074
if correct_ans == final_ans_brute:
    print "Brute method works"
if correct_ans == final_ans_heat:
    print "Heat method works"
else:
    print(final_ans_heat)

print("----------\n")

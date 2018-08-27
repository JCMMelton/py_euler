
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

def file_open():
    with open('p067_triangle.txt') as file_raw:
        en_file = [line for line in file_raw]
    return en_file

numsf = file_open()

numbers_raw = numsf
#.split('\n')

# print numbers_raw
# print len(numbers_raw)

numbers = []
for n in numbers_raw:
    if n == '':
        continue
    numbers.append([int(i) for i in n.split(' ')])

# print numbers
# print len(numbers)
# exit()

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

def heat(numbers):
    nodes = build_nodes(numbers)
    for n1 in range(len(nodes)-2, 0, -1):
        for n2 in range(0, len(nodes[n1])):
            print (nodes[n1][n2].a, nodes[n1+1][n2].a, nodes[n1+1][n2+1].a)
            if nodes[n1+1][n2].a > nodes[n1+1][n2+1].a:
                nodes[n1][n2].a += nodes[n1+1][n2].a
            else:
                nodes[n1][n2].a += nodes[n1+1][n2+1].a
    if nodes[1][0].a > nodes[1][1].a:
        ans = nodes[0][0].a + nodes[1][0].a
    else:
        ans = nodes[0][0].a + nodes[1][1].a
    return ans



print heat(numbers)

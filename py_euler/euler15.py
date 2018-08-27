
def opaths(n):
    ans = 0
    index = end = n-1
    grid = [n for x in range(0, n)]
    while True:
        if grid[0] == 0:
            break
        if grid[index] == 0:
            grid[index-1] = grid[index-1]-1
            for x in range(index, end):
                grid[x] = grid[index-1]
            index = end
        else:
            ans += grid[index]
            grid[index] = 0
            index -= 1
        print grid
    print grid
    return ans

def paths(n):
    ans = 0
    j = n+1
    for i in range(1, n+2):
        ans += i * j
        print str(j) + " " + str(i)
        j -= 1
    return ans

def lattice(x):
    grid = [x for i in range(0, x)]
    index = 0
    count = 0
    while True:
      if grid[index] > 0:
        count += grid[index]
        grid[index] = 0
      else:
        index += 1
        if grid[index] > 0:
          grid[index] -= 1
          count += 1
          for i in range(0, index):
            grid[i] = grid[index]
          index = 0
      if index == len(grid)-1:
        count += 1
        break
    return count

def blocks(x):
    grid = [[0 for n in range(0, x)] for n in range(0, x)]
    grid[0][0] = 2
    for i in range(1, x):
        grid[i][0] = i+2
        grid[0][i] = i+2
    for i in range(1, x):
        for j in range(1, x):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    # print(grid)
    print(grid[x-1][x-1])

blocks(20)

# print(lattice(3))
# print(lattice(20))

# print paths(2)
# print paths(3)
# print paths(5)

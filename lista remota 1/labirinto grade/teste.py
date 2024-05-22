def connected(maze, i, p, k):
    while k:
        if 'X' in maze[i]:
            j = maze[i].index('X')
            maze[i][j], p = '.', [(i,j)]
            k -= 1
            break
        i += 1
    while k:
        x,y = p.pop()
        for i,j in ((x,y-1),(x,y+1),(x-1,y),(x+1,y)):
            if 0 <= i< n and 0 <= j < m and maze[i][j] == 'X':
                maze[i][j] = '.'
                p.append((i,j))
                k -= 1
                if k == 0:
                    break

def add_walls(maze, n, m, k):
    maze = [['X' if cell == '.' else cell for cell in row] for row in maze]
    k = n * m - k - sum(i.count('#') for i in maze)
    connected(maze, 0, [], k)
    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

n, m, k = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]
print_maze(add_walls(maze, n, m, k))
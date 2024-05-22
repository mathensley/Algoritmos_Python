from collections import deque
import random, time

def bfs(maze, start, end):
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    queue = deque([(start)])
    visited = set([start])
    
    while queue:
        cell = queue.popleft()
        if cell == end:
            return True
        for direction in directions:
            next_cell = (cell[0] + direction[0], cell[1] + direction[1])
            if (0 <= next_cell[0] < len(maze) and 
                0 <= next_cell[1] < len(maze[0]) and
                maze[next_cell[0]][next_cell[1]] == '.' and 
                next_cell not in visited):
                queue.append(next_cell)
                visited.add(next_cell)
    
    return False

def dfs(i, j, empty_cells, rows, cols):
    stack = [(i, j)]
    visited = set()
        
    while stack:
        cell = stack.pop()
        if cell not in visited:
            visited.add(cell)
            x, y = cell
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.' and (nx, ny) not in visited:
                    stack.append((nx, ny))
        
    return len(visited) == len(empty_cells)

"""
def check_connectivity(maze):
    rows = len(maze)
    cols = len(maze[0])
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == '.':
                return dfs(i, j, rows, cols)
    
    return True
"""


def check_connectivity(maze):
    rows = len(maze)
    cols = len(maze[0])
    empty_cells = [(i, j) for i in range(rows) for j in range(cols) if maze[i][j] == '.']
    
    if not empty_cells:
        return True
    
    start = random.choice(empty_cells)
    return dfs(start[0], start[1], empty_cells, rows, cols)


'''
def check_connectivity(maze):
    start = None
    end = None
    result = False
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '.':
                start = (i, j)
                break
        if start:
            break
    
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i,j) != start and maze[i][j] == '.':
                end = (i, j)
                result = bfs(maze, start, end)
                if not result:
                    return result
    return result
'''

'''
def add_walls(maze, k):
    i = 0
    count = 0
    while i < len(maze):
        for j in range(len(maze[0])):
            if maze[i][j] == '.' and count <= k:
                maze[i][j] = 'X'
                if not check_connectivity(maze):
                    maze[i][j] = '.'
                else:
                    count += 1
                    i = 0
                    break
            if (j+1) == len(maze[0]):
                i += 1
                break
        if count == k:
            break
    return maze
'''


def add_walls(maze, k):
    rows = len(maze)
    cols = len(maze[0])
    count = 0
    
    while count < k:
        i = random.randint(0, rows - 1)
        j = random.randint(0, cols - 1)
        
        if maze[i][j] == '.':
            maze[i][j] = 'X'
            if not check_connectivity(maze):
                maze[i][j] = '.'
            else:
                count += 1
    return maze



def print_maze(maze):
    for row in maze:
        print("".join(row))

def measure_time(maze):
    start_time = time.time()
    print_maze(add_walls(maze, k))
    end_time = time.time()
    return (end_time - start_time) * 1000
    

n, m, k = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]
#print_maze(add_walls(maze, k))
print(measure_time(maze))
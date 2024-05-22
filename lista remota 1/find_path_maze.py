from queue import Queue
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import time

def bfs(maze, start, end):
    queue = Queue()
    queue.put([start])            
    while queue:
        path = queue.get()
        x, y = path[-1]
        if (x, y) == end:
            return path
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            next_x, next_y = x + dx, y + dy
            if next_x < 0 or next_x >= len(maze) or next_y < 0 or next_y >= len(maze[0]):
                continue
            if maze[next_x][next_y] != "#" and (next_x, next_y) not in path:
                new_path = list(path)
                new_path.append((next_x, next_y))
                queue.put(new_path)


def print_maze(maze):
    for row in maze:
        print("".join(['*' if cell == "." else '█' for cell in row]))

def print_maze_with_path(maze, path):
    path_set = set(path)
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) in path_set:
                print('•', end='')
            else:
                print('█' if cell == '#' else '*', end='')
        print()

def draw_maze(maze, path):
    cmap = ListedColormap(['white', 'gray', 'blue']) # Vazio - Parede - Caminho
    maze_array = np.array(maze)
    for x, y in path:
        maze_array[x,y] = 2 # o caminho encontrado
    plt.imshow(maze_array, cmap=cmap)
    plt.xticks([]), plt.yticks([])
    plt.show()

def draw_maze_steps(maze, path):
    cmap = ListedColormap(['white', 'gray', 'blue']) # Vazio - Parede - Caminho
    maze_array = np.array(maze)
    fig, ax = plt.subplots()
    for step in path:
        x, y = step
        maze_array[x,y] = 2
        ax.imshow(maze_array, cmap=cmap)
        ax.set_xticks([]), ax.set_yticks([])
        plt.pause(0.75)
        plt.draw()
    

def transform_maze(maze):
    new_maze = []
    for row in maze:
        c_row = []
        for cell in row:
            if cell == '#':
                c_row.append(1)
            else:
                c_row.append(0)
        new_maze.append(c_row)
    return new_maze



maze = [
        ['#', '.', '.', '#'],
        ['.', '.', '#', '.'],
        ['#', '.', '.', '.']
        ]
start = (0,1)
end = (1,3)
path = bfs(maze, start, end)
print(path)
print_maze(maze)
print("-" * (len(maze[0])+1))
print_maze_with_path(maze, path)
#draw_maze(transform_maze(maze), path)
draw_maze_steps(transform_maze(maze), path)
"""
Implementar os métodos de busca em largura e profundidade para uma ambiente de "labirinto".

Habilidade desenvolvida: compreender como utilizar os métodos de busca na resolução de um problema.

O método deve executar em um ambiente composto por uma matriz quadrada de ordem n (até 10). 
Células com valor "1" representarão lugares que o agente não poderá percorrer. 
A célula com valor 2 representa o local de onde o agente iniciará e a célula de valor 3 o lugar onde ele precisa chegar.
Considere o custo de passo com valor igual para qualquer movimentação e que será permitida a movimentação em quadro direções 
(cima, baixo, esquerda e direita). A implementação deve ter uma função sucessor e uma função de teste de objetivo.

"""

import pygame
from utils import maze_setup
from depth import depth_search, improve_depth_search_path
from breadth import breadth_search, improve_breadth_search_path


MAZE1 = [
    [0, 1, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

MAZE2 = [
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0, 3, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


MAZES = [MAZE1, MAZE2]

# -----------PYGAME----------
      
"""
This function is responsible for drawing the maze on the screen.
It loops through all the maze cells and paints them according to their values.
White squares are walkable paths (value = 1), black ones are walls (value = 0), green is the start point (value = 2),
red is the goal (value = 3), and yellow (gold) represents the final path found by the search algorithm.
"""
def draw_maze(improved_path, maze):
    for r in range(ROWS):
        for c in range(COLS):
            color = WHITE if maze[r][c] == 1 else BLACK
            if (r, c) == start:
                color = GREEN
            if (r, c) in improved_path:
                color = pygame.Color(255, 215, 0, 255)
            if (r, c) == goal:
                color = RED
            pygame.draw.rect(screen, color, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

"""
This function takes the full path visited by the algorithm and visualizes it step by step in blue.
"""
def draw_path(path):
    for r, c in path:
        pygame.draw.rect(screen, BLUE, (c * CELL_SIZE + 10, r * CELL_SIZE + 10, CELL_SIZE - 20, CELL_SIZE - 20))
        pygame.display.update()
        pygame.time.delay(100)
        
"""
Main game loop that runs the search and visualizes both Depth Search and Breadth Search algorithms for all mazes.
"""        
running = True
while running:
    for i in range(len(MAZES)):
        start, goal = maze_setup(MAZES[i])
        print(f" --- MAZE {i} INFO\n")
        print(f"Start: {start} | Goal: {goal}\n")
        
        # ------------------------ DEPTH SEARCH ------------------------
        dfs_path = depth_search(MAZES[i], start, goal)
        improved_dfs_path = improve_depth_search_path(dfs_path.copy())

        ROWS, COLS = len(MAZES[i]), len(MAZES[i][0])    
        CELL_SIZE = 50
        WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
        WHITE, BLACK, GREEN, RED, BLUE = (255, 255, 255), (0, 0, 0), (0, 255, 0), (255, 0, 0), (0, 0, 255)
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        screen.fill(BLACK)

        pygame.display.set_caption("Depth Search")
        draw_maze(improved_dfs_path, MAZES[i])
        draw_path(dfs_path)
        pygame.time.wait(1000)

        # ------------------------ BREADTH SEARCH ------------------------
        bfs_path = breadth_search(MAZES[i], start, goal)
        improved_bfs_path = improve_breadth_search_path(bfs_path.copy())

        screen.fill(BLACK)
        pygame.display.set_caption("Breadth Search")
        draw_maze(improved_bfs_path, MAZES[i])
        draw_path(bfs_path)
        pygame.time.wait(1000)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

pygame.quit()
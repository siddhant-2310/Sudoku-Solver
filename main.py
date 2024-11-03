import pygame
from solver import solve  

WIDTH = 550
background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)
buffer = 5

grid = [[0, 0, 4, 0, 0, 3, 1, 0, 7],
        [7, 0, 2, 5, 9, 4, 3, 8, 6],
        [0, 0, 0, 0, 0, 8, 9, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 7, 5, 0, 0, 0, 8, 3, 0],
        [8, 3, 6, 2, 0, 9, 4, 0, 1],
        [5, 6, 0, 0, 0, 0, 7, 1, 0],
        [0, 0, 0, 8, 0, 0, 0, 9, 0],
        [0, 0, 1, 7, 3, 6, 0, 0, 0]]

# Copy of the original grid
original_grid = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

def insert(win, position):
    i, j = position[1], position[0]
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if original_grid[i-1][j-1] != 0:
                    return
                if event.key == pygame.K_0:  # Checking for 0
                    grid[i-1][j-1] = 0
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    pygame.display.update()
                    return
                if pygame.K_1 <= event.key <= pygame.K_9:  # Valid input
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    value = myfont.render(str(event.key - pygame.K_0), True, (0, 0, 0))
                    win.blit(value, (position[0]*50 + 15, position[1]*50))
                    grid[i-1][j-1] = event.key - pygame.K_0
                    pygame.display.update()
                    return
                return

def draw_grid(win, grid):
    # Draw the grid lines
    for i in range(0, 10):
        if i % 3 == 0:
            pygame.draw.line(win, (0, 0, 0), (50, i * 50 + 50), (WIDTH - 50, i * 50 + 50), 4)
            pygame.draw.line(win, (0, 0, 0), (i * 50 + 50, 50), (i * 50 + 50, WIDTH - 50), 4)
        pygame.draw.line(win, (0, 0, 0), (50, i * 50 + 50), (WIDTH - 50, i * 50 + 50), 2)
        pygame.draw.line(win, (0, 0, 0), (i * 50 + 50, 50), (i * 50 + 50, WIDTH - 50), 2)

    # Render numbers on the grid
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if 0 < grid[i][j] < 10:
                if original_grid[i][j] != 0:  # Original value
                    value = myfont.render(str(grid[i][j]), True, (0, 0, 255))  # Blue color
                else:
                    value = myfont.render(str(grid[i][j]), True, (0, 0, 0))  # Black color
                win.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

def reset_grid_to_original(grid):
    # Reset only non-original values
    for i in range(9):
        for j in range(9):
            if original_grid[i][j] == 0:
                grid[i][j] = 0

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Sudoku")
    win.fill(background_color)

    draw_grid(win, grid)

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Clear the window
                    win.fill(background_color)
                    pygame.display.update()

                    # Reset the grid and solve it
                    reset_grid_to_original(grid)
                    solve(grid)

                    # Redraw the solved grid
                    draw_grid(win, grid)
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()

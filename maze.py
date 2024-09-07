import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
window_size = (600, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Maze Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Maze Design 
maze = '
##########
#S       #
#       # #
#       # #
#       # #
#       # #
#     #   #
##        # 
#     E   #
##########
'

# Process maze layout
maze = maze.strip().splitlines()

# Dimensions
cell_size = min(window_size[0] // len(maze[0]), window_size[1] // len(maze))
player_pos = [0, 0]  # Will be set by 'S' in the maze

# Find starting position
for y, row in enumerate(maze):
    for x, char in enumerate(row):
        if char == 'S':
            player_pos = [x, y]

def draw_maze():
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if char == '#':
                pygame.draw.rect(screen, BLACK, rect)
            elif char == 'E':
                pygame.draw.rect(screen, RED, rect)

def draw_player():
    rect = pygame.Rect(player_pos[0] * cell_size, player_pos[1] * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, BLUE, rect)

def main():
    running = True

    while running:
        screen.fill(WHITE)
        draw_maze()
        draw_player()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_pos = [player_pos[0] - 1, player_pos[1]]
                elif event.key == pygame.K_RIGHT:
                    new_pos = [player_pos[0] + 1, player_pos[1]]
                elif event.key == pygame.K_UP:
                    new_pos = [player_pos[0], player_pos[1] - 1]
                elif event.key == pygame.K_DOWN:
                    new_pos = [player_pos[0], player_pos[1] + 1]
                else:
                    new_pos = player_pos

                # Check if new position is within bounds and not a wall
                if maze[new_pos[1]][new_pos[0]] != '#':
                    player_pos[:] = new_pos

                # Check for victory
                if maze[player_pos[1]][player_pos[0]] == 'E':
                    print("Congratulations! You've reached the exit!")
                    running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

import pygame
import random

# Initialize pygame
pygame.init()

# Define screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Pac-Man parameters
PACMAN_SIZE = 20
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
pacman_speed = 5

# Ghost parameters
ghost_size = 20
ghosts = [{'x': 50, 'y': 50, 'color': RED, 'direction': 'right'}]  # Simplified for now

# Maze layout (just a simple grid for now)
maze = [
    "####################",
    "#........#.........#",
    "#.#######.#.#######.#",
    "#........#.........#",
    "#.#######.#.#######.#",
    "#........#.........#",
    "####################",
]

# Define the font for text
font = pygame.font.SysFont("comicsansms", 25)

# Function to draw Pac-Man
def draw_pacman(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), PACMAN_SIZE)

# Function to draw ghosts
def draw_ghosts():
    for ghost in ghosts:
        pygame.draw.circle(screen, ghost['color'], (ghost['x'], ghost['y']), ghost_size)

# Function to draw maze
def draw_maze():
    block_size = 30  # Each grid block is 30x30
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                pygame.draw.rect(screen, BLUE, (x * block_size, y * block_size, block_size, block_size))

# Main game loop
def game_loop():
    global pacman_x, pacman_y, ghosts

    running = True
    while running:
        screen.fill(BLACK)
        draw_maze()
        draw_pacman(pacman_x, pacman_y)
        draw_ghosts()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            pacman_x -= pacman_speed
        if keys[pygame.K_RIGHT]:
            pacman_x += pacman_speed
        if keys[pygame.K_UP]:
            pacman_y -= pacman_speed
        if keys[pygame.K_DOWN]:
            pacman_y += pacman_speed

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()

# Run the game
game_loop()

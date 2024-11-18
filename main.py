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
PACMAN_SIZE = 15
pacman_x, pacman_y = 60, 60  # Start position
pacman_speed = 5

# Ghost parameters
ghost_size = 15
ghosts = [{'x': 120, 'y': 120, 'color': RED, 'direction': 'right'}]

# Maze layout (30x30 block grid)
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

# Pellet parameters
pellet_size = 5
pellets = []

# Generate pellets based on maze layout
block_size = 30  # Each grid block is 30x30
for y, row in enumerate(maze):
    for x, cell in enumerate(row):
        if cell == '.':
            pellets.append({'x': x * block_size + block_size // 2, 'y': y * block_size + block_size // 2})

# Function to draw Pac-Man
def draw_pacman(x, y):
    pygame.draw.circle(screen, YELLOW, (x, y), PACMAN_SIZE)

# Function to draw ghosts
def draw_ghosts():
    for ghost in ghosts:
        pygame.draw.circle(screen, ghost['color'], (ghost['x'], ghost['y']), ghost_size)

# Function to draw maze
def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                pygame.draw.rect(screen, BLUE, (x * block_size, y * block_size, block_size, block_size))

# Function to draw pellets
def draw_pellets():
    for pellet in pellets:
        pygame.draw.circle(screen, WHITE, (pellet['x'], pellet['y']), pellet_size)

# Check for wall collisions
def can_move(x, y):
    grid_x = x // block_size
    grid_y = y // block_size
    if maze[grid_y][grid_x] == '#':
        return False
    return True

# Move ghosts randomly
def move_ghosts():
    for ghost in ghosts:
        directions = ['left', 'right', 'up', 'down']
        if ghost['direction'] == 'left':
            if can_move(ghost['x'] - ghost_size, ghost['y']):
                ghost['x'] -= pacman_speed
            else:
                ghost['direction'] = random.choice(directions)
        elif ghost['direction'] == 'right':
            if can_move(ghost['x'] + ghost_size, ghost['y']):
                ghost['x'] += pacman_speed
            else:
                ghost['direction'] = random.choice(directions)
        elif ghost['direction'] == 'up':
            if can_move(ghost['x'], ghost['y'] - ghost_size):
                ghost['y'] -= pacman_speed
            else:
                ghost['direction'] = random.choice(directions)
        elif ghost['direction'] == 'down':
            if can_move(ghost['x'], ghost['y'] + ghost_size):
                ghost['y'] += pacman_speed
            else:
                ghost['direction'] = random.choice(directions)

# Main game loop
def game_loop():
    global pacman_x, pacman_y, ghosts

    score = 0
    running = True
    while running:
        screen.fill(BLACK)
        draw_maze()
        draw_pacman(pacman_x, pacman_y)
        draw_ghosts()
        draw_pellets()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Pac-Man movement with collision
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and can_move(pacman_x - pacman_speed, pacman_y):
            pacman_x -= pacman_speed
        if keys[pygame.K_RIGHT] and can_move(pacman_x + pacman_speed, pacman_y):
            pacman_x += pacman_speed
        if keys[pygame.K_UP] and can_move(pacman_x, pacman_y - pacman_speed):
            pacman_y -= pacman_speed
        if keys[pygame.K_DOWN] and can_move(pacman_x, pacman_y + pacman_speed):
            pacman_y += pacman_speed

        # Check for pellet collision
        pellets[:] = [pellet for pellet in pellets if not (abs(pacman_x - pellet['x']) < PACMAN_SIZE and abs(pacman_y - pellet['y']) < PACMAN_SIZE)]
        score = len(pellets)

        # Move ghosts
        move_ghosts()

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()

# Run the game
game_loop()

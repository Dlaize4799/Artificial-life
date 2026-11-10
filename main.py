import pygame

pygame.init()

WIDTH = 900
HEIGHT = 600
COLUMNS = 60
ROWS = 40
CELL_SIZE = 15

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Artificial Life')

clock = pygame.time.Clock()

running = True

# ROWS counts the number of rows present and hence how deep we can go (y-coordinate)
# This may seem counter-intuitive ROWS associated with y? but remember it is number of rows:)
world = [   [0 for y in range(ROWS)] # Inner list represent a column
        for x in range(COLUMNS)    ]

for x in range(10, 20):
    for y in range(10, 20):
        world[x][y] = 3

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False

    screen.fill((20, 30, 20)) 

    for x in range(COLUMNS):
            for y in range(ROWS):
    
                food = world[x][y]
    
                if food > 0:
    
                    pixel_x = x * CELL_SIZE
                    pixel_y = y * CELL_SIZE
    
                    green = 40 + food * 35
                    color = (20, green, 30)
    
                    pygame.draw.rect(screen, color, (pixel_x, pixel_y, 15, 15))

    # vertical lines
    for i in range(COLUMNS):
        pygame.draw.line(screen, (0, 0, 0), (15 + 15 * i, 0), (15 + 15 * i, 600))
    # Horizontal lines
    for i in range(ROWS):
        pygame.draw.line(screen, (0, 0, 0), (0, 15 + i * 15), (900, 15 + i * 15))
    
    pygame.display.flip()  

    clock.tick(60)

pygame.quit()
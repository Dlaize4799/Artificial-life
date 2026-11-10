import pygame
from environment import Environment
from config import WIDTH, HEIGHT, COLUMNS, ROWS, CELL_SIZE

environment = Environment()

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Artificial Life')

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False

    screen.fill((20, 30, 20)) 

    for x in range(COLUMNS):
            for y in range(ROWS):
    
                food_ = environment.food[x][y]
    
                if food_ > 0:
    
                    pixel_x = x * CELL_SIZE
                    pixel_y = y * CELL_SIZE
    
                    green = 40 + food_ * 35
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
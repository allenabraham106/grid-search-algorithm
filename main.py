import pygame 
pygame.init()

WINDOW_HEIGHT = int(input("What would you like the height to be: "))
WINDOW_WIDTH = int(input("What would you like the width to be: "))
cell_dimension = int(input("What size do you want the cells to be: "))
white_colour = (200, 200, 200)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Our window")

def draw_grid(surface):
    for x in range(0, WINDOW_WIDTH, cell_dimension):
        pygame.draw.line(surface, white_colour, (x, 0), (x,WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, cell_dimension):
        pygame.draw.line(surface, white_colour, (0, y), (WINDOW_WIDTH, y))
program_run = True

while program_run:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_run = False
    
    draw_grid(window)
    pygame.display.flip()
pygame.quit()

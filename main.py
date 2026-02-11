import pygame 
pygame.init()

WINDOW_HEIGHT = int(input("What would you like the height to be: "))
WINDOW_WIDTH = int(input("What would you like the width to be: "))

window = pygame.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
pygame.display.set_caption("Our window")
program_run = True

while program_run:
    pygame.time.delay(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_run = False
        
pygame.quit()

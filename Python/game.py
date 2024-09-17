import pygame

screenWidth = 400
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))

run = True

white = (255,255,255)
black = (0,0,0)

while run:
    
    screen.fill(white)
    pygame.draw.rect(screen, black)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
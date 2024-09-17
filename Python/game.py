import pygame

screenWidth = 400
screenHeight = 600

# screen = pygame.display.set_mode((screenWidth, screenHeight))
screen = pygame.display.set_mode((screenWidth, screenHeight) ,pygame.SCALED)

run = True

white = (255,255,255)
black = (0,0,0)

baseRect = pygame.Rect((0,0,400,10))

while run:
    
    screen.fill(white)
    pygame.draw.rect(screen, black, baseRect)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
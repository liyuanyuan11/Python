import pygame
pygame.init()
windowSurface = pygame.display.set_mode([500,400])
BLACk = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
windowSurface.fill(WHITE)
pygame.draw.rect(windowSurface,RED,(60,200,200,100),1)
pygame.display.update()
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
pygame.quit()
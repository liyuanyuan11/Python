import pygame
pygame.init()
windowSurface = pygame.display.set_mode([500,400])
BLACk = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
windowSurface.fill(WHITE)
pygame.draw.polygon(windowSurface,GREEN,((300,100),(445,206),(391,377),(210,377),(154,206)))
pygame.display.update()
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
pygame.quit()
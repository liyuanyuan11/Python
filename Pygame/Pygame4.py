import pygame
pygame.init()
windowSurface = pygame.display.set_mode([500,400])
BLACk = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
windowSurface.fill(WHITE)
pygame.draw.line(windowSurface,BLACk,(60,60),(60,120),2)
pygame.draw.line(windowSurface,RED,(60,90),(90,90),2)
pygame.draw.line(windowSurface,BLACk,(90,60),(90,120),2)
pygame.display.update()
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
pygame.quit()
import pygame
pygame.init()
windowSurface=pygame.display.set_mode([500,400])
Running=True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
pygame.quit()
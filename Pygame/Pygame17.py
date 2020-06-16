import pygame
pygame.init()
windowSurface = pygame.display.set_mode([800,600])
YELLOW = (255,255,0)
BLACK = (0,0,0)
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                point = event.pos
                pygame.draw.circle(windowSurface,YELLOW,point,10)
            if pygame.mouse.get_pressed()[2]:
                windowSurface.fill(BLACK)
    pygame.display.update()
pygame.quit()
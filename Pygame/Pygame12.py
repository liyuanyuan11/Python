import pygame
pygame.init()
windowSurface = pygame.display.set_mode([800,600])
pic = pygame.image.load("/Users/chenchaoyang/Desktop/python/Python/Photo/dog1.jpg")
picX = 0
picY = 200
BLACK = (0,0,0)
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    windowSurface.fill(BLACK)
    picX += 1
    windowSurface.blit(pic,(picX,picY))
    pygame.display.update()
pygame.quit()
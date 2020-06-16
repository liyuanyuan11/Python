import pygame
pygame.init()
windowSurface = pygame.display.set_mode([800,600])
pic = pygame.image.load("/Users/chenchaoyang/Desktop/python/Photo/dog1.jpg")
windowSurface.blit(pic,(100,200))
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    pygame.display.update()
pygame.quit()
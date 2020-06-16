import pygame
pygame.init()
windowSurface = pygame.display.set_mode([800,600])
pic = pygame.image.load("/Users/chenchaoyang/Desktop/python/Photo/dog1.jpg")
picX = 0
picY = 200
BLACK = (0,0,0)
speed = 5
timer = pygame.time.Clock()
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    windowSurface.fill(BLACK)
    picX += speed
    if picX +pic.get_width() >= 800:
        speed = -speed
        pic = pygame.image.load("/Users/chenchaoyang/Desktop/python/Photo/dog2.jpg")
    elif picX <= 0:
        speed = -speed
        pic = pygame.image.load("/Users/chenchaoyang/Desktop/python/Photo/dog1.jpg")
    windowSurface.blit(pic,(picX,picY))
    pygame.display.update()
    timer.tick(60)
pygame.quit()
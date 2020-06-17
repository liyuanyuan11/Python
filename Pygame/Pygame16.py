import pygame
pygame.init()
windowSurface = pygame.display.set_mode((800,600))
pic = pygame.image.load("/Users/chenchaoyang/Desktop/python/Python/Photo/dog1.jpg")
BLACK = (0,0,0)
WHITE = (255,255,255)
myString = "Hello World!"
font = pygame.font.SysFont("Times New Roman",48)
text = font.render(myString,True,WHITE)
picX = 0
picY = 0
speed = 1
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Running = False
            if event.key == pygame.K_LEFT:
                moveLeft = True
            if event.key == pygame.K_RIGHT:
                moveRight = True
            if event.key == pygame.K_UP:
                moveUp = True
            if event.key == pygame.K_DOWN:
                moveDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
            if event.key == pygame.K_RIGHT:
                moveRight = False
            if event.key == pygame.K_UP:
                moveUp = False
            if event.key == pygame.K_DOWN:
                moveDown = False
    if moveDown and text.get_height() + picY < 600:
        picY += speed
    if moveUp and picY > 0:
        picY -= speed
    if moveLeft and picX > 0:
        picX -= speed
    if moveRight and text.get_width() + picY < 800:
        picX += speed
    windowSurface.fill(BLACK)    
    windowSurface.blit(text,(picX,picY))
    pygame.display.update()
pygame.quit()
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_ESCAPE:
        Running = False
    if event.key == pygame.K_LEFT:
        moveLeft = True
    if event.key == pygame.K_RIGHT:
        moveRight = True
    if event.key == pygame.K_UP:
        moveUp = True
    if event.key == pygame.K_DOWN:
        moveDown = True
if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT:
        moveLeft = False
    if event.key == pygame.K_RIGHT:
        moveRight = False
    if event.key == pygame.K_UP:
        moveUp = False
    if event.key == pygame.K_DOWN:
        moveDown = False
if moveDown and text.get_height() + picY < 600:
    picY += speed
if moveUp and picY > 0:
    picY -= speed
if moveLeft and picX > 0:
    picX -= speed
if moveRight and text.get_width() + picY < 800:
    picX += speed         
windowSurface.fill(BLACK)
windowSurface.blit(text(picX,picY))
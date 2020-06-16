import pygame
pygame.init()
windowSurface = pygame.display.set_mode([500,400])
music = pygame.mixer.Sound("/Users/chenchaoyang/Desktop/python/Music/Music2.wav")
music.play()
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                music.stop() 
    pygame.display.update()
pygame.quit()
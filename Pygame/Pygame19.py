import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
WHITE = (255,255,255)
BLACK = (0,0,0)
ball = pygame.image.load("/Users/chenchaoyang/Desktop/python/Photo/pingpang2.png")
ballx = 0
bally = 0
speedx = 5
speedy = 5
paddlew = 100
paddleh = 15
paddlex = 300
paddley = 570
font = pygame.font.SysFont("stsong", 26)
ZiTi=pygame.font.get_fonts()
for i in ZiTi:
   print(i)
timer = pygame.time.Clock()
points = 0
lives = 3
pop = pygame.mixer.Sound("/Users/chenchaoyang/Desktop/python/Music/Music2.wav")
pop.play()
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] and paddlew < 400:
                paddlew = paddlew*2
            elif pygame.mouse.get_pressed()[2] and paddlew > 20:
                paddleh = paddlew/2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                lives = 3
                points = 0
                pop.play()
    if lives == 0:
        text = font.render("游戏结束",True,WHITE)
        screen.blit(text,(350,270))
        pygame.display.update()
        pop.stop()
        continue
    ballx += speedx
    bally += speedy
    if ballx <= 0 or ballx + ball.get_width() >= 800:
        speedx = -speedx
    if bally + ball.get_height() >= 600:
        lives -= 1
        speedy = -speedy
    if bally <= 0:
        speedy = -speedy
    screen.fill(BLACK)
    screen.blit(ball,(ballx,bally))
    paddlex = pygame.mouse.get_pos()[0]
    pygame.draw.rect(screen,WHITE,(paddlex,paddley,paddlew,paddleh))
    if bally + ball.get_height() >= paddley and speedy > 0:
        if ballx + ball.get_width() / 2 >= paddlex and ballx + ball.get_width() / 2 <= paddlex + paddlew:
            points += 1
            speedy = -speedy
    draw_string = "生命数:" + str(lives) + "得分:" + str(points)
    text = font.render(draw_string,True,WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text,text_rect)
    pygame.display.update()
    timer.tick(60)
pygame.quit()
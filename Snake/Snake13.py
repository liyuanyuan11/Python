import pygame
import random
import sys
pygame.init()
WHITE = (255,255,255)
GREEN = (0,255,0)
DARKGREEN = (0,185,0)
YELLOW = (255,255,0)
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
windowsWidth = 800
windowsHeight = 600
cellSize = 20
mapWidth = int(windowsWidth / cellSize)
mapHeight = int(windowsHeight / cellSize)
HEAD = 0
snakeSpeed
def main():
    pygame.init()
    screen = pygame.display.set_mode((windowsWidth,windowsHeight))
    pygame.display.set_caption("贪吃蛇")
    screen.fill(WHITE)
    snakeSpeedClock = pygame.time.Clock()
    startGame(screen)
    while True:
        music = pygame.mixer.Sound("/Users/chenchaoyang/Desktop/python/Python/Music/Music2.wav") 
        music.play(-1)
        runGame(screen,snakeSpeedClock)
        music.stop()
        gameOver(screen)
def startGame(screen):
    gameStart = pygame.image.load("/Users/chenchaoyang/Desktop/python/Python/Photo/Snake start.jpg")
    screen.blit(gameStart,(70,30))
    font = pygame.font.SysFont("SimHei",40)
    tip = font.render("按任意键开始游戏",True,(65,105,225))
    screen.blit(tip,(240,550))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    terminate()
                else:
                    return
def runGame(screen,snakeSpeedClock):
    startX = random.randint(3,mapWidth - 8)
    startY = random.randint(3,mapHeight - 8)
    snakeCoords = [{"x": startX,"y":startY},
           {"x": startX - 1,"y":startY},
           {"x": startX - 2,"y":startY}]
    direction = RIGHT
    food = {"x":random.randint(0,mapWidth - 1),"y":random.randint(0,mapHeight - 1)}
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT
                elif event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN      
                elif event.key == pygame.K_ESCAPE:
                    terminate()
        moveSnake(direction,snakeCoords)
        isEattingFood(snakeCoords,food)
        ret = isAlive(snakeCoords)
        if not ret:
            break
        gameRun = pygame.image.load("/Users/chenchaoyang/Desktop/python/Python/Photo/Snake.jpg")
        screen.blit(gameRun,(0,0))
        drawFood(screen,food)
        drawSnake(screen,snakeCoords)
        drawScore(screen,len(snakeCoords) - 3)
        pygame.display.update()
        snakeSpeedClock.tick(snakeSpeed)
def drawFood(screen,food):
    x = food["x"] * cellSize
    y = food["y"] * cellSize
    pygame.draw.rect(screen,YELLOW,(x,y,cellSize,cellSize))
def drawSnake(screen,snakeCoords):
    for coord in snakeCoords:
        x = coord["x"] * cellSize
        y = coord["y"] * cellSize
        pygame.draw.rect(screen,DARKGREEN,(x,y,cellSize,cellSize))
        pygame.draw.rect(screen,GREEN,(x + 4,y + 4,cellSize - 8,cellSize - 8))
def drawScore(screen,score):
    font = pygame.font.SysFont("SimHei",30)
    scoreSurf = font.render("得分:" + str(score),True,WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (windowsWidth - 200,50)
    screen.blit(scoreSurf,scoreRect)
def moveSnake(direction,snakeCoords):
    if direction == UP:
        newHead = {"x":snakeCoords[HEAD]["x"],"y":snakeCoords[HEAD]["y"] - 1}
    elif direction == DOWN:
        newHead = {"x":snakeCoords[HEAD]["x"],"y":snakeCoords[HEAD]["y"] + 1}
    elif direction == LEFT:
        newHead = {"x":snakeCoords[HEAD]["x"] - 1,"y":snakeCoords[HEAD]["y"]}
    elif direction == RIGHT:
        newHead = {"x":snakeCoords[HEAD]["x"] + 1,"y":snakeCoords[HEAD]["y"]}
    snakeCoords.insert(0,newHead)

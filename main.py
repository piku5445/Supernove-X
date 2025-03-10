import pygame
import random
#initalizing the pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
#background
bg=pygame.image.load('back.jpg')

#Title and icon
pygame.display.set_caption('Supernova X ')
icon=pygame.image.load('spacecraft.png')
pygame.display.set_icon(icon)
##adding player image
playerImg=pygame.image.load('spacecraft.png')
playerX=370
playerY=480
player_changeX=2

##adding enemy image
enemyImg=pygame.image.load('alien.png')
enemyX=random.randint(0,800)
enemyY=random.randint(50,150)
enemy_changeX=0.3
enemy_changeY=40

##adding bullet image
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=480
bullet_changeY=0.3
bullet_state = "ready"  # "ready" - you can't see the bullet on the screen, "fire" - the bullet is moving

def enemy(x,y):
    screen.blit(enemyImg,(x,y))
def player(x,y):
    screen.blit(playerImg,(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))



running=True
while running:
    screen.fill((42,21,23))
    screen.blit(bg,(0,0))
    
    for event in pygame.event.get() :
        if event.type==pygame.QUIT:
            running=False        
                 
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_changeX=-3
            if event.key==pygame.K_RIGHT:
                player_changeX=3
            if event.key==pygame.K_UP:
                playerY=playerY-50 
            if event.key==pygame.K_DOWN:
                playerY=playerY+50   
            if event.key==pygame.K_SPACE:
                if bullet_state == "ready":
                    #get the current x coordinate of the space ship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                player_changeX=0

    #checking for boundaries
    playerX += player_changeX
    if playerX >= 800 - playerImg.get_width():
        playerX = 800 - playerImg.get_width()
    elif playerX <= 0:
        playerX = 0

    enemyX += enemy_changeX
    if enemyX <= 0:
        enemy_changeX = 0.3
        enemyY += enemy_changeY
    elif enemyX >= 800 - enemyImg.get_width():
        enemy_changeX = -0.3
        enemyY += enemy_changeY

    # to shoot the multiple bullet Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_changeY
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    enemy(enemyX, enemyY)
    player(playerX, playerY)
    
    pygame.display.update()


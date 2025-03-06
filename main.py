import pygame
#initalizing the pygame
pygame.init()
screen=pygame.display.set_mode(((800,600)))
running =True

#Title and icon
pygame.display.set_caption('Supernova X ')
icon=pygame.image.load('spacecraft.png')
pygame.display.set_icon(icon)
##adding player image
playerImg=pygame.image.load('spacecraft.png')
playerX=370
playerY=480
player_changeX=0

##adding enemy image
enemyImg=pygame.image.load('play.png')
enemyX=370
enemyY=480
enemy_changeX=0
#adding bullet image
bulletImg=pygame.image.load('ufo.png')
def player(x,y):
    screen.blit(playerImg,(x,y))
def bullet(x,y):

    screen.blit(bulletImg,(x,y))

# def bullet_Fire(y):
#     bullet(playerX,y)
#     i=0
#     while y<0:
#         i=i+1    
# def collision(x,y):
#     if x>=0         
running=True

while running:

    screen.fill((42,21,23))

    
    for event in pygame.event.get() :
        if event.type==pygame.QUIT:
            running=False        
                 
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_changeX=-0.1
            if event.key==pygame.K_RIGHT:
                player_changeX=0.1
            if event.key==pygame.K_UP:
                playerY=playerY-50 
            if event.key==pygame.K_DOWN:
                playerY=playerY+50   
            # if event.key==pygame.K_SPACE:
            #     bullet_Fire(playerY)
       


    playerX=playerX+player_changeX
    if playerX >= 800 - playerImg.get_width():
        playerX = 800 - playerImg.get_width()
    elif playerX <= 0:
        playerX = 0
 
        
    # bullet(playerX,playerY)
    player(playerX,playerY) 
     
    pygame.display.update()        

import pygame
import pygame.display as display
import pygame.event as pygame_event

import random

#Initialize the pygame
pygame.init()

#Sreen dimentions
screen_height = 600
screen_width = 800

#Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

#Background Image
background = pygame.image.load('background.png')

#Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo_32.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('battleship.png')
playerX = 370
playerY = 480
player_speed = 15
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('ufo_64.png')
enemyX = random.randint(0, screen_width)
enemyY = random.randint(50, 150)
enemy_X_speed = 12
enemy_Y_speed = 40
enemyX_change = enemy_X_speed
enemyY_change = enemy_Y_speed

#Missile
missileImg = pygame.image.load('missile.png')
missileX = 0
missileY = 480
missileX_change = 0
missileY_change = 10
missile_state = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_missile(x, y):
    global missile_state
    missile_state = "fire"
    screen.blit(missileImg, (x + 16, y + 10))

#Game Loop
running = True
while running:

    #RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    #Drawing Background Image
    screen.blit(background, (0,0))

    for event in pygame_event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed, check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = - player_speed
            if event.key == pygame.K_RIGHT:
                playerX_change = player_speed
            if event.key == pygame.K_SPACE:
                fire_missile(playerX, missileY)

        # if the keystroke is released, stop moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #Checking for boundaries 
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= (screen_width - 64):  # 64 is the image width
        playerX = (screen_width - 64)

    #Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = enemy_X_speed
        enemyY += enemyY_change
    elif enemyX >= (screen_width - 64):  # 64 is the image width
        enemyX_change = -enemy_X_speed
        enemyY += enemyY_change

    #Missile movement
    if missile_state is "fire":
        fire_missile(playerX, missileY)
        missileY -= missileY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    display.update()

import pygame
import time
import random
import numpy as np

pygame.init()

velocity = 5
display_width = 810
display_height = 510

arena_x = 805
arena_y = 505

bot_scale = 0.1125
bot_height = 52
bot_width = 48

radius = 25

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('ERA-IITK')

carImg = pygame.image.load('racecar.png')

# carImg = pygame.transform.rotozoom(carImg, 90, 1)

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False

x = 30
y = 480

x_change = 0
y_change = 0

screen = pygame.display.set_mode((display_width, display_height))
# carImg = pygame.draw.circle(screen , black, (x, y), radius)

direction = 0

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def rev_bot_dim():
    global x
    global y 
    
    x = x+y
    y = x-y
    x = x-y
    
def car(x,y):
    global carImg
    global black
    
    carImg = pygame.draw.circle(screen, black, (x, y), radius)
        
def move_up():
    global x_change
    global y_change
    global velocity
    
    x_change = 0
    y_change = -velocity
    
def move_down():
    global x_change
    global y_change
    global velocity
    
    x_change = 0
    y_change = velocity
    
def move_right():
    global x_change
    global y_change
    global velocity
    
    x_change = velocity
    y_change = 0

def move_left():
    global x_change
    global y_change
    global velocity
    
    x_change = -velocity
    y_change = 0
    
def boundary():
    global x_change
    global y_change
    global x
    global y
    
    if (x-radius+x_change)<5 or (x+radius+x_change)>805 or (y+radius+y_change)>505 or (y-radius+y_change)<5:
        x_change=0
        y_change=0
        
    if ((x+radius+x_change)>455 and (x-radius+x_change)<480) and (y-radius+y_change)<105:
        x_change=0
        y_change=0
        
    if ((x+radius+x_change)>145 and (x-radius+x_change)<170) and (y-radius+y_change)<365 and (y+radius+y_change)>265:
        x_change=0
        y_change=0
        
    if ((x+radius+x_change)>640 and (x-radius+x_change)<665) and (y-radius+y_change)<245 and (y+radius+y_change)>145:
        x_change=0
        y_change=0
        
    if ((x+radius+x_change)>330 and (x-radius+x_change)<355) and (y-radius+y_change)<505 and (y+radius+y_change)>405:
        x_change=0
        y_change=0
        
    if ((x+radius+x_change)>125 and (x-radius+x_change)<225) and (y-radius+y_change)<130 and (y+radius+y_change)>105:
        x_change=0
        y_change=0
        
    if ((x+radius+x_change)>355 and (x-radius+x_change)<455) and (y-radius+y_change)<267.5 and (y+radius+y_change)>242.5:
        x_change=0
        y_change=0
        
    if ((x+radius+x_change)>585 and (x-radius+x_change)<685) and (y-radius+y_change)<430 and (y+radius+y_change)>405:
        x_change=0
        y_change=0
    
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction=4
            elif event.key == pygame.K_RIGHT:
                direction=3
            elif event.key == pygame.K_UP:
                direction = 1
            elif event.key == pygame.K_DOWN:
                direction = 2
        
        elif event.type == pygame.KEYUP:
            direction=0

    gameDisplay.fill(white)
        
    things(0, 0, display_width, display_height, black)
    things(5, 5, 800, 500, white)
    
    things(455, 5, 25, 100, black)
    things(145, 265, 25, 100, black)
    things(640, 145, 25, 100, black)
    things(330, 405, 25, 100, black)
    
    things(125, 105, 100, 25, black)
    things(355, 242.5, 100, 25, black)
    things(585, 405, 100, 25, black)
    
           
        
    if direction == 1:
        move_up()
    elif direction == 2:
        move_down()
    elif direction == 3:
        move_right()
    elif direction == 4:
        move_left()
    elif direction == 0:
        x_change=0
        y_change=0
    
    boundary() 

    x+= x_change
    y+= y_change
    
    car(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
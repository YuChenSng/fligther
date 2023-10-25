import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('mickey and yuchen')


#load images
sun_img = pygame.image.load('img/sun.jpg')
bg_img  = pygame.image.load('img/sky.jpg')

run = True
while run:
    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run =  False

    pygame.display.update()

# Git Hud commit 2
# Git Hud Commit 3

pygame.quit() 

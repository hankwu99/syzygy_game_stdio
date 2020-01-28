import sys
import pygame
from pygame.locals import QUIT
from pygame.color import THECOLORS

def play():
    pygame.init() # pygame初始化

    window = pygame.display.set_mode((1400, 1080)) # pygame screen size
    windowcaption = pygame.display.set_caption('Syzygy Music') #screen name
    window.fill((0, 0, 0))

    background = pygame.Surface(window.get_size()) #背景畫布
    background.convert()
    background.fill((0, 0, 0))
    window.blit(background,(0, 0)) 

    pygame.draw.rect(window, THECOLORS['white'], [340, 0, 120 , 1080], 1)
    pygame.draw.rect(window, THECOLORS['white'], [460, 0, 120 , 1080], 1)
    pygame.draw.rect(window, THECOLORS['white'], [580, 0, 120 , 1080], 1)
    pygame.draw.rect(window, THECOLORS['white'], [700, 0, 120 , 1080], 1)
    pygame.draw.rect(window, THECOLORS['white'], [820, 0, 120 , 1080], 1)
    pygame.draw.rect(window, THECOLORS['white'], [940, 0, 120 , 1080], 1)

    pygame.draw.rect(window, THECOLORS['white'], [340, 540, 720 , 5], 0)




    pygame.display.update() 

    while True:  # 視窗關閉設定
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

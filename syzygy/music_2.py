import sys
import pygame as pg
from pygame.locals import QUIT
from pygame.color import THECOLORS

def play():
    pg.init()

    #main screen setting
    window = pg.display.set_mode((1400, 1014)) 
    windowcaption = pg.display.set_caption('Syzygy Music') 
    window.fill((0, 0, 0))
    background = pg.Surface(window.get_size())
    background.convert()
    background.fill((0, 0, 0))
    window.blit(background,(0, 0)) 

    #music name
    game_name = pg.font.SysFont('Agency FB', 40)
    text = game_name.render("DaDaDaDaDaDaDaDaDaDa", True, THECOLORS['white'])
    background.blit(text, [10, 5])

    #music play 
    pg.mixer.init()
    pg.mixer.music.set_volume(0.7) 
    pg.mixer.music.load('打打打打打打打打打打.mp3')
    pg.mixer.music.play()

    #key painting
    pg.draw.rect(background, THECOLORS['white'], [340, 0, 120 , 1014], 1)
    pg.draw.rect(background, THECOLORS['white'], [460, 0, 120 , 1014], 1)
    pg.draw.rect(background, THECOLORS['white'], [580, 0, 120 , 1014], 1)
    pg.draw.rect(background, THECOLORS['white'], [700, 0, 120 , 1014], 1)
    pg.draw.rect(background, THECOLORS['white'], [820, 0, 120 , 1014], 1)
    pg.draw.rect(background, THECOLORS['white'], [940, 0, 120 , 1014], 1)
    pg.draw.line(background, [255, 255, 255], [340, 507], [1059, 507], 5)

    #FPS
    fps_clock = pg.time.Clock() 

    running = True
    while running:  # 視窗關閉設定
        fps_clock.tick(50)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                runing = False
            window.blit(background, (0, 0))
            pg.display.update() 
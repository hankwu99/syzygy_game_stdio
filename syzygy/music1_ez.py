import sys, time, pygame as pg
from pygame.locals import QUIT

#global def
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
place_y = 0

def play():
    pg.init()

    # main screen setting
    window = pg.display.set_mode((1100, 1014)) 
    pg.display.set_caption('Syzygy Music') 
    window.fill((0, 0, 0))
    background = pg.Surface(window.get_size())
    background.convert()
    background.fill((0, 0, 0))
    window.blit(background,(0, 0)) 

    # music name
    game_name = pg.font.SysFont('Agency FB', 38)
    text = game_name.render("Lost Sky - Where We Started", True, BLACK, WHITE)
    background.blit(text, [10, 20])

    # score
    score = pg.font.SysFont('Agency FB', 30)
    text = score.render("Score:", True, WHITE)
    background.blit(text, [10, 80])

    # music play 
    pg.mixer.init()
    pg.mixer.music.set_volume(0.5) 
    pg.mixer.music.load('source/game music/Where We Started.mp3')
    pg.mixer.music.play()

    # tap class
    class tap(pg.sprite.Sprite):
        def __init__(self, key_place, place):
            # key_palce = 軌道座標, 340 = 第一軌道 其他以key painting的460、580..類推
            super().__init__()
            # 載入圖片
            self.raw_image = pg.image.load('source/image/tap.png').convert_alpha()
            # 是上方的音符還是下方的音符
            if place == 'top':
                place_y = -20
            elif place == 'bottom':
                place_y = 994
            # 定位
            background.blit(self.raw_image, (key_place, place_y))
    
    # key painting
    pg.draw.rect(background, WHITE, [340, 0, 120 , 1014], 1)
    pg.draw.rect(background, WHITE, [460, 0, 120 , 1014], 1)
    pg.draw.rect(background, WHITE, [580, 0, 120 , 1014], 1)
    pg.draw.rect(background, WHITE, [700, 0, 120 , 1014], 1)
    pg.draw.rect(background, WHITE, [820, 0, 120 , 1014], 1)
    pg.draw.rect(background, WHITE, [940, 0, 120 , 1014], 1)
    pg.draw.line(background, WHITE, [340, 507], [1059, 507], 5)

    tap1 = tap(340, 'top')

    # game loop
    while True:
        pg.time.Clock().tick(50) # FPS
        window.blit(background, (0, 0))
        pg.display.update() 
        for event in pg.event.get(): # quit the game
            if event.type == pg.QUIT:
                pg.quit()
                exit()
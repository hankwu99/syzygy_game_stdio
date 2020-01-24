import sys
import pygame
from pygame.locals import QUIT

# 初始化
pygame.init()

window_surface = pygame.display.set_mode((800, 1000))
pygame.display.set_caption('Syzygy Music')
window_surface.fill((0, 0, 0))

# 宣告 font 文字物件
head_font = pygame.font.SysFont(None, 60)
# 渲染方法會回傳 surface 物件
text_surface = head_font.render('                            Syzygy', True, (255, 255, 255))
# blit 用來把其他元素渲染到另外一個 surface 上，這邊是 window 視窗
window_surface.blit(text_surface, (10, 10))

# 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）
pygame.display.update()

# 視窗關閉設定
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

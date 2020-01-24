import sys
import pygame
from pygame.locals import QUIT
import tkinter as tk


def game():
    pygame.init() # 初始化

    window_surface = pygame.display.set_mode((800, 1000))
    pygame.display.set_caption('Syzygy Music')
    window_surface.fill((0, 0, 0))
   
    pygame.display.update()  # 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）

    while True:  # 視窗關閉設定
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

window=tk.Tk()
window.title('Syzygy Music')
window.geometry('800x1000')
window.configure(background='black')

title_label = tk.Label(window, text = 'Syzygy Music', font = ('Kaiso-Next-B', 50), width = 70, height = 6)
title_label.pack()

button_start = tk.Button(window, text = "開始遊戲", font = ('Noto Serif CJK TC', 20), width = 10, height = 2, command = game)
button_start.pack()

window.mainloop()

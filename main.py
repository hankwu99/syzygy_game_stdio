import sys
import pygame
from pygame.locals import QUIT
import tkinter as tk
import time

#------------------------------------------------------Pygame area code --------------------------------------------------------#

def game():
    window.destroy()
    pygame.mixer.music.stop()
    pygame.init() # pygame初始化

    window_surface = pygame.display.set_mode((800, 1000)) # pygame screen size
    pygame.display.set_caption('Syzygy Music') #screen name
    window_surface.fill((0, 0, 0))
   
    pygame.display.update()  # 更新畫面，等所有操作完成後一次更新（若沒更新，則元素不會出現）

    while True:  # 視窗關閉設定
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

#------------------------------------------------------Pygame area code --------------------------------------------------------#

#-------------------------------------------------------Main menu code ---------------------------------------------------------#

pygame.mixer.init() # 背景音樂播放
pygame.mixer.music.set_volume(0.7) # 音量大小0 ~ 1

if not pygame.mixer.music.get_busy(): #如果沒有在播放音樂 就播放
    pygame.mixer.music.load('Inspirational.mp3')
    pygame.mixer.music.play()

window=tk.Tk()
window.title('Syzygy Music')
window.geometry('800x1000')
window.configure(background='black')
window.resizable(False, False)

title_label = tk.Label(window, text = 'Syzygy Music Game', font = ('skuare', 30), width = 70, height = 6)
title_label.pack()

label = tk.Label(window, bg = "black", font = ('skuare', 50), width = 50, height = 3)
label.pack()

button_start = tk.Button(window, text = "Start", font = ('skuare', 20), width = 10, height = 2, command = game)
button_start.pack()

_label = tk.Label(window, bg = "black", font = ('skuare', 50), width = 50, height = 1)
_label.pack()

button_quit = tk.Button(window, text = "Quit", font = ('skuare', 20), width = 10, height = 2, command = window.destroy)
button_quit.pack()

author_label = tk.Label(window, text = 'Made By Syzygy Games Studio', font = ('skuare', 18), width = 1000, height = 5)
author_label.pack(side='bottom')
author_label.pack()

window.mainloop()

#-------------------------------------------------------Main menu code ---------------------------------------------------------#

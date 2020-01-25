import sys
import pygame
from pygame.locals import QUIT
import tkinter as tk
from tkinter import PhotoImage
import time

#------------------------------------------------------Pygame area code---------------------------------------------------------#

def game_music1():
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

def game_music2():
    window.destroy()
    pygame.mixer.music.stop()
    pygame.init() 

    window_surface = pygame.display.set_mode((800, 1000)) 
    pygame.display.set_caption('Syzygy Music') 
    window_surface.fill((0, 0, 0))
   
    pygame.display.update() 

    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

#------------------------------------------------------Pygame area code---------------------------------------------------------#

#------------------------------------------------------Music menu code----------------------------------------------------------#
def music1():
    if pygame.mixer.music.get_busy(): #如果在播放音樂 就播放
        pygame.mixer.music.stop()
        pygame.mixer.music.load('riot.mp3')
        pygame.mixer.music.play()

def music2():
    if pygame.mixer.music.get_busy(): #如果在播放音樂 就播放
        pygame.mixer.music.stop()
        pygame.mixer.music.load('KVDS-Move.mp3')
        pygame.mixer.music.play()

def music_menu():
    menu = tk.Toplevel(window)
    menu.title('Music Menu')
    menu.geometry('800x1000')
    menu.resizable(False, False)

    label = tk.Label(menu, text = 'Music Menu', font = ('skuare', 30), width = 70, height = 3)

    music1_name = tk.Label(menu, text = 'Music1\nR・I・O・T by Raise a Suilen', font = ('skuare', 20), width = 70, height = 2)
    # 無法放音樂封面圖 暫時無解
    music1_play = tk.Button(menu, text = '試聽一段', font = ('微軟正黑體', 15), width = 10, height = 1, command = music1)
    music1_game = tk.Button(menu, text = 'play this', font = ('skuare', 15), width = 10, height = 1, command = game_music1)

    __label = tk.Label(menu, font = ('skuare', 10), width = 50, height = 2)

    music2_name = tk.Label(menu, text = 'Music2\nKVDS - Move', font = ('skuare', 20), width = 70, height = 2)
    # 無法放音樂封面圖 暫時無解
    music2_play = tk.Button(menu, text = '試聽一段', font = ('微軟正黑體', 15), width = 10, height = 1, command = music2)
    music2_game = tk.Button(menu, text = 'play this', font = ('skuare', 15), width = 10, height = 1, command = game_music2)

    label.pack()
    music1_name.pack()
    music1_play.pack()
    music1_game.pack()
    __label.pack()
    music2_name.pack()
    music2_play.pack()
    music2_game.pack()
        
#------------------------------------------------------Music menu code----------------------------------------------------------#

#-------------------------------------------------------Main menu code----------------------------------------------------------#

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
label = tk.Label(window, bg = "black", font = ('skuare', 50), width = 50, height = 3)
button_start = tk.Button(window, text = "Start", font = ('skuare', 20), width = 10, height = 2, command = music_menu)
_label = tk.Label(window, bg = "black", font = ('skuare', 50), width = 50, height = 1)
button_quit = tk.Button(window, text = "Quit", font = ('skuare', 20), width = 10, height = 2, command = window.destroy)
author_label = tk.Label(window, text = 'Made By Syzygy Games Studio', font = ('skuare', 18), width = 1000, height = 5)
author_label.pack(side='bottom')

title_label.pack()
label.pack()
button_start.pack()
_label.pack()
button_quit.pack()
author_label.pack()
window.mainloop()

#-------------------------------------------------------Main menu code----------------------------------------------------------#

import tkinter as tk, sys, pygame, time
from tkinter import PhotoImage
from pygame.locals import QUIT
import music1_ez, music1_nor

#------------------------------------------------------Pygame area code---------------------------------------------------------#

def game_music1_ez():
    background.destroy() 
    pygame.mixer.music.fadeout(50)
    music1_ez.play() # customize module

def game_music1_normal():
    background.destroy()
    pygame.mixer.music.fadeout(50)
    music1_nor.play() # customize module

#------------------------------------------------------Pygame area code---------------------------------------------------------#
#------------------------------------------------------Music menu code----------------------------------------------------------#
def music():
    pygame.mixer.music.fadeout(50)
    pygame.mixer.music.load('source/game music/Where We Started.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

def music_menu():
    menu = tk.Toplevel(background)
    menu.title('Music Menu')
    menu.geometry('900x1014')
    menu.resizable(False, False)

    label = tk.Label(menu, text = 'Music Menu', font = ('Agency FB', 30), width = 70, height = 3)
    music1_name = tk.Label(menu, text = 'Music_1\nLost Sky - Where We Started feat. Jex', font = ('Agency FB', 20), width = 70, height = 2)
    music1_play = tk.Button(menu, text = '試聽一段', font = ('Agency FB', 15), width = 15, height = 1, command = music)
    music1_ez = tk.Button(menu, text = 'easy', font = ('Agency FB', 20), width = 10, height = 1, command = game_music1_ez)
    music1_normal = tk.Button(menu, text = 'normal', font = ('Agency FB', 20), width = 10, height = 1, command = game_music1_normal)

    label.pack()
    music1_name.pack()
    music1_play.pack()
    music1_ez.pack()
    music1_normal.pack()

#------------------------------------------------------Music menu code----------------------------------------------------------#
#------------------------------------------------------information code---------------------------------------------------------#

def info():
    info = tk.Toplevel(background)
    info.title('More Information')
    info.geometry('900x600')
    info.resizable(False, False)

    label = tk.Label(info, text = 'More Information', font = ('Agency FB', 30), width = 70, height = 3)
    paragraph = tk.Label(info, 
    text = """
    Syzygy Games Studio
    是一群來自台灣的高中學生
    閒來沒事想用Python寫音樂遊戲ww
    願你在這世界被溫柔以待
    """, font = ('Agency FB', 20), width = 70, height = 10)

    label.pack()
    paragraph.pack()

#------------------------------------------------------information code---------------------------------------------------------#
#-------------------------------------------------------Main menu code----------------------------------------------------------#

background=tk.Tk()
background.title('Music')
background.geometry('900x1014')
background.configure(background='black')
background.resizable(False, False)

pygame.mixer.init()
pygame.mixer.music.set_volume(0.7) 
pygame.mixer.music.load('source/background music/Inspirational.mp3')
pygame.mixer.music.play()

title_label = tk.Label(background, text = 'Music Game', font = ('Agency FB', 50), width = 50, height = 4)

label = tk.Label(background, bg = "black", font = ('Agency FB', 40), width = 50, height = 1)
button_start = tk.Button(background, text = "Start", font = ('Agency FB', 20), width = 15, height = 2, command = music_menu)

_label = tk.Label(background, bg = "black", font = ('Agency FB', 40), width = 50, height = 1)
button_info = tk.Button(background, text = "More Info.", font = ("Agency FB", 20), width = 15, height = 2, command = info)

__label = tk.Label(background, bg = "black", font = ('Agency FB', 40), width = 50, height = 1)
button_quit = tk.Button(background, text = "Quit", font = ('Agency FB', 20), width = 15, height = 2, command = background.destroy)

version = tk.Label(background, bg = "black", fg= "white", text = 'Beta v 0.0.0', font = ("Agency FB", 18), width = 1000, height = 1)
version.pack(side='bottom')

author_label = tk.Label(background, text = 'Made By Syzygy Games Studio', font = ('Agency FB', 18), width = 1000, height = 3)
author_label.pack(side='bottom')

title_label.pack()

label.pack()
button_start.pack()

_label.pack()
button_info.pack()

__label.pack()
button_quit.pack()

author_label.pack()

version.pack()

background.mainloop()

#-------------------------------------------------------Main menu code----------------------------------------------------------#
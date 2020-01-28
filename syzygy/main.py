import tkinter as tk
from tkinter import PhotoImage
import sys
import pygame
from pygame.locals import QUIT
import music_1
import music_2

#------------------------------------------------------Pygame area code---------------------------------------------------------#

def game_music1():
    window.destroy()
    pygame.mixer.music.stop()
    music_1.play() # customize module

def game_music2():
    window.destroy()
    pygame.mixer.music.stop()
    music_2.play() # customize module

#------------------------------------------------------Pygame area code---------------------------------------------------------#

#------------------------------------------------------Music menu code----------------------------------------------------------#
def music1():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('riot.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

def music2():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('KVDS-Move.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

def music_menu():
    menu = tk.Toplevel(window)
    menu.title('Music Menu')
    menu.geometry('900x1000')
    menu.resizable(False, False)

    label = tk.Label(menu, text = 'Music Menu', font = ('Agency FB', 30), width = 70, height = 3)

    music1_name = tk.Label(menu, text = 'Music_1\nR・I・O・T by Raise a Suilen', font = ('Agency FB', 20), width = 70, height = 2)
    music1_play = tk.Button(menu, text = '試聽一段', font = ('Agency FB', 15), width = 15, height = 1, command = music1)
    music1_game = tk.Button(menu, text = 'play this', font = ('Agency FB', 20), width = 10, height = 1, command = game_music1)

    ___label = tk.Label(menu, font = ('Agency FB', 10), width = 50, height = 2)

    music2_name = tk.Label(menu, text = 'Music_2\nKVDS - Move', font = ('Agency FB', 20), width = 70, height = 2)
    music2_play = tk.Button(menu, text = '試聽一段', font = ('Agency FB', 15), width = 15, height = 1, command = music2)
    music2_game = tk.Button(menu, text = 'play this', font = ('Agency FB', 20), width = 10, height = 1, command = game_music2)

    label.pack()

    music1_name.pack()
    music1_play.pack()
    music1_game.pack()

    ___label.pack()

    music2_name.pack()
    music2_play.pack()
    music2_game.pack()
        
#------------------------------------------------------Music menu code----------------------------------------------------------#

#------------------------------------------------------information code---------------------------------------------------------#

def info():
    info = tk.Toplevel(window)
    info.title('More Information')
    info.geometry('700x700')
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

pygame.mixer.init()
pygame.mixer.music.set_volume(0.7) 

if not pygame.mixer.music.get_busy():
    pygame.mixer.music.load('Inspirational.mp3')
    pygame.mixer.music.play()

window=tk.Tk()
window.title('Music')
window.geometry('900x1000')
window.configure(background='black')
window.resizable(False, False)

title_label = tk.Label(window, text = 'Music Game', font = ('Agency FB', 50), width = 50, height = 4)

label = tk.Label(window, bg = "black", font = ('Agency FB', 40), width = 50, height = 1)
button_start = tk.Button(window, text = "Start", font = ('Agency FB', 20), width = 15, height = 2, command = music_menu)

_label = tk.Label(window, bg = "black", font = ('Agency FB', 40), width = 50, height = 1)
button_info = tk.Button(window, text = "More Info.", font = ("Agency FB", 20), width = 15, height = 2, command = info)

__label = tk.Label(window, bg = "black", font = ('Agency FB', 40), width = 50, height = 1)
button_quit = tk.Button(window, text = "Quit", font = ('Agency FB', 20), width = 15, height = 2, command = window.destroy)

version = tk.Label(window, bg = "black", fg= "white", text = 'Beta v 0.0.0', font = ("Agency FB", 18), width = 1000, height = 1)
version.pack(side='bottom')

author_label = tk.Label(window, text = 'Made By Syzygy Games Studio', font = ('Agency FB', 18), width = 1000, height = 3)
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

window.mainloop()

#-------------------------------------------------------Main menu code----------------------------------------------------------#
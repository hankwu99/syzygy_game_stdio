import sys
import pygame
from pygame.locals import QUIT
import tkinter as tk
from tkinter import PhotoImage

def play():
    pygame.init() # pygame初始化

    window_surface = pygame.display.set_mode((900, 1000)) # pygame screen size
    pygame.display.set_caption('Syzygy Music') #screen name
    window_surface.fill((0, 0, 0))

    background = pygame.Surface(window_surface.get_size()) #背景畫布
    background.convert()
    background.fill((0, 0, 0))
    window_surface.blit(background,(0, 0)) 

    pygame.display.update() 

    while True:  # 視窗關閉設定
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

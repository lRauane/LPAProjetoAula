#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pygame


from code.const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Loop end')
                    pygame.quit()
                    quit()
            menu = Menu(self.window)
            menu.run()
            pass

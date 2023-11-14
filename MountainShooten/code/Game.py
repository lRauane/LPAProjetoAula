#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame as pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                pass
            else:
                pygame.quit()
                sys.exit()
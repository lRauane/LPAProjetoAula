import sys

import pygame.display
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.entity_list: list[Entity] = []
        self.mode = menu_option  # opção do menu / 1 ou 2 players
        self.name = name

        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        pass

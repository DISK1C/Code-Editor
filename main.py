"""
This is a code editor made in python using pygame

Author: DISK1C
Status: planning
"""

__author__ = "DISK1C"
__status__ = "planning"

import sys

import pygame
from pygame.locals import *

from src.settings import *
from src.file import file

class app:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.file = file(self, "hello.txt")

    def render(self):
        self.screen.fill((0, 0, 0))

    def update(self):
        events = list(pygame.event.get())
        for ev in events:
            quit() if ev.type == QUIT else None
        
        pygame.display.set_caption(str(self.clock.get_fps()))

        self.clock.tick(60)
        pygame.display.flip()

    def run(self):
        while True:
            self.render()
            self.file.update()
            self.update()

if __name__ == '__main__':
    app().run()
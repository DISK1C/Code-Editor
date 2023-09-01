"""
this file contains some basic functionality of a file like:
rendering, typing, syntax highlighting etc....
"""

import pygame
from pygame.locals import *

class file:
    
    def __init__(self, app, filename:str) -> None:
        self.app = app
        self.line_index = 0
        self.character_index = 0
        self.line = ""
        self.placeholder = []
        self.data = [""]

    def render(self):
        print('rendering')

    def new_line(self):
        pass

    def delete_line(self):
        pass

    def handle_events(self):
        pass

    def update(self):
        self.handle_events()
        self.render()
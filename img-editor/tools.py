from PIL import ImageDraw
from widgets import *
import pygame

using = None
mouse_down = False
color = black

class Tool():
    def __init__(self):
        self.click = self.drag = self.release = (lambda self, img, pos: None)

class Pen(Tool):
    def __init__(self):
        self.last_pos = None
        self.width = 4
        self.click = self.draw
        self.drag = self.draw
        self.mode = 'p'
    def draw(self, image, pos):
        if self.mode == 'e': self.color = white
        else: self.color = color
        x, y = pos
        draw = ImageDraw.Draw(image)
        if self.last_pos:
            draw.line((self.last_pos, pos), self.color, self.width)
        self.last_pos = pos
    def release(self, image, pos):
        self.last_pos = None

pen = Pen()
rotate = Tool()

# handling events
def event_handler(event, image):
    global mouse_down

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_down = True
        print("using", using)

        if using:
            using.click(image, event.pos)


    elif event.type == pygame.MOUSEMOTION:
        if mouse_down and using:
            using.drag(image, event.pos)

    elif event.type == pygame.MOUSEBUTTONUP:
        mouse_down = None
        if using:
            using.release(image, event.pos)

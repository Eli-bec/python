from PIL import ImageDraw
from widgets import *
import pygame

mouse_down = False
color = black

# the super class of all the tools
class Tool():
    def click(self, img, pos):
        pass
    def drag(self, img, pos):
        pass
    def release(self, img, pos):
        pass
    def draw(self, surface):
        pass

class Pen(Tool):
    def __init__(self):
        super().__init__()

        self.last_pos = None
        self.width = 4
        self.click = self.drag = self.pen_down
        self.mode = 'p'
    def pen_down(self, image, pos):
        if self.mode == 'e': self.color = white
        else: self.color = color
        x, y = pos
        draw = ImageDraw.Draw(image)
        if self.last_pos:
            draw.line((self.last_pos, pos), self.color, self.width)
        self.last_pos = pos
    def release(self, image, pos):
        self.last_pos = None

class Crop(Tool):
    def __init__(self):
        self.click = self.start_select
        self.drag = self.selecting
        self.start_pos = None
        self.pos = None
        self.selected = False
    def start_select(self, image, pos):
        self.start_pos = pos
        self.pos = None
    def selecting(self, image, pos):
        self.pos = pos
    def release(self, image, pos):
        if self.selected and self.pos == None:
            self.selected = False
            self.start_pos = None
            self.pos = None
        elif self.start_pos and self.pos and self.start_pos != self.pos:
            self.selected = True
    def crop(self, image):
        x1, y1 = self.in_img(image, *self.start_pos)
        x2, y2 = self.in_img(image, *self.pos)
        image = image.crop((x1, y1, x2, y2))
        self.start_pos = None
        self.pos = None
        self.selected = False
        return image
    def draw(self, surface):
        if self.start_pos and self.pos:
            x, y = self.start_pos
            w, h = self.pos[0] - x, self.pos[1] - y
            pygame.draw.rect(surface, black, (x, y, w, h), 1)
    def in_img(self, image, x, y):
        if x < 0:
            x = 0
        elif x >= image.width:
            x = image.width - 1
        if y < 0:
            y = 0
        elif y >= image.height:
            y = image.height - 1
        return (x, y)

pen = Pen()
rotate = Tool()
crop = Crop()

using = Tool()

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

def draw(surface):
    using.draw(surface)

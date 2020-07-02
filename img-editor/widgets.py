import pygame

white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
gray = (230, 230, 230, 255)

# image width: 32, image height: 32

class Button:
    '''
    x, y, width, height, image
    '''
    def __init__(self, image, command, key, alt_command=(lambda: None), alt_image = None):
        self.x, self.y = 0, 0
        self.w, self.h = 64, 64
        self.img = image
        self.pressed = False
        self.cmd = command
        self.alt_cmd = alt_command
        self.key = key
        self.alt_img = alt_image

    def draw(self, surface, alt):
        rect = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(surface, gray, rect)
        if alt and self.alt_img:
            surface.blit(self.alt_img, (self.x + 16, self.y + 16))
        else:
            surface.blit(self.img, (self.x + 16, self.y + 16))
        if self.pressed:
            pygame.draw.rect(surface, black, rect, 1)
        else:
            points = (
                (self.x, self.y + self.h),
                (self.x + self.w, self.y + self.h),
                (self.x + self.w, self.y))
            pygame.draw.lines(surface, black, False, points, 2)

    def click(self, pos):
        x, y = pos
        if self.x <= x < self.x + self.w and self.y <= y < self.y + self.h:
            return True
        else:
            return False

    def config(self, x, y):
        self.x, self.y = x, y

'''
class Rot_Button(Button):
    @property
    def pressed(self):
        return self._pressed
    @pressed.setter
    def press(self, value):

'''

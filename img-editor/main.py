import pygame
import os.path
import tools

from PIL import Image
from widgets import *
from tkinter import Tk
from tkinter.filedialog import (askopenfilename,
                                asksaveasfilename)
from tkinter.colorchooser import askcolor

win_width = 800
win_height = 800

running = True
alt = False # check if 'alternate'(alt) key pressed
title = "Image Editor"

pygame.init()
# when the tkinter.filedialog module is use, a tk window will appear. the following line is used for closing it.
Tk().withdraw()

filepath = None
image = None # image in pillow
image_display = None # image in pygame, class: pygame.Surface

# button icons
img_open = pygame.image.load("images\\img_open.png")
img_save = pygame.image.load("images\\img_save.png")
img_pen  = pygame.image.load("images\\img_pen.png")
img_erase = pygame.image.load("images\\img_erase.png")
img_color = pygame.Surface((32,32))
img_color.fill(black)
img_c_rotate = pygame.image.load("images\\img_c_rotate.png")
img_a_rotate = pygame.image.load("images\\img_a_rotate.png")
img_crop = pygame.image.load("images\\img_crop.png")

# initialize the window
window = pygame.display.set_mode((win_width, win_height), pygame.RESIZABLE)
pygame.display.set_caption(title)

# command for buttons
def cmd_open():
    filename = askopenfilename()
    if os.path.exists(filename):
        global filepath, image, image_display, title
        print("opening {}".format(filename))
        image = Image.open(filename)
        title = "Image Editor ({})".format(filename)
        pygame.display.set_caption(title)
        print("Succeed")
        filepath = filename

def cmd_save():
    if filepath:
        pass
    else:
        cmd_save_as()

def cmd_save_as():
    filename = asksaveasfilename()
    pass

def cmd_pen():
    tools.using = tools.pen
    tools.pen.mode = 'p'

def cmd_erase():
    tools.using = tools.pen
    tools.pen.mode = 'e'

def cmd_color():
    color = askcolor()[0]
    if color:
        color = tuple(map(int, color))
        tools.color = color
        img_color.fill(color)

def cmd_c_rotate():
    print("clockwise rotation")
    global image
    if image:
        image = image.rotate(-90)

def cmd_a_rotate():
    global image
    if image:
        image = image.rotate(90)

def cmd_crop():
    pass

# rearrange the widgets when window resize
def wid_adjust():
    for li, line in enumerate(widgets):
        pad_x = 32*li
        y = 68*li + win_height - 136
        for i, wid in enumerate(line):
            x = pad_x + i*68
            wid.config(x, y)

def wid_get():
    return widgets[0] + widgets[1]

# I call the list widgets but it seems that there are only buttons
widgets = [[
        Button(img_open, cmd_open, pygame.K_a),
        Button(img_save, cmd_save, pygame.K_s, cmd_save_as),
        Button(img_pen, cmd_pen, pygame.K_d, cmd_erase, img_erase),
        Button(img_color, cmd_color, pygame.K_f)], [
        Button(img_c_rotate, cmd_c_rotate, pygame.K_z),
        Button(img_a_rotate, cmd_a_rotate, pygame.K_x),
        Button(img_crop, cmd_crop, pygame.K_c)
    ]
]

wid_adjust()

# mainloop
while running:
    for event in pygame.event.get():
        # handling quit event
        if event.type == pygame.QUIT:
            running = False

        # handling mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pressed = False
            for wid in wid_get():
                if wid.click(event.pos):
                    wid.pressed = event.button
                    pressed = True
                    break
            if not pressed:
                tools.event_handler(event, image)

        # handling mouse release
        elif event.type == pygame.MOUSEBUTTONUP:
            press = False
            for wid in wid_get():
                if wid.pressed:
                    wid.pressed = 0
                    if wid.click(event.pos):
                        pressed = True
                        if event.button == 3 or alt:
                            wid.alt_cmd()
                        elif event.button == 1:
                            wid.cmd()
            if not pressed:
                tools.event_handler(event, image)

        # handling window resize
        elif event.type == pygame.VIDEORESIZE:
            win_width, win_height = event.size
            if win_width < 320:
                win_width = 320
            if win_height < 256:
                win_height = 256
            pygame.display.set_mode((win_width, win_height), pygame.RESIZABLE)
            wid_adjust()

        # handling key press
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                alt = True

        # handling key release
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                alt = False

        # handling mouse motion
        elif event.type == pygame.MOUSEMOTION:
            tools.event_handler(event, image)


    # TODO: tools.use()

    # Draw
    window.fill(white)
    if image:
        raw_str = image.tobytes("raw")
        image_display = pygame.image.frombuffer(raw_str, image.size, image.mode)
        window.blit(image_display, (0,0))
    for wid in wid_get():
        wid.draw(window, alt)

    pygame.display.update()

pygame.quit()

import pygame

class GameObject:
    """ object that contains a position """
    def __init__(self, x, y):
        self.x, self.y = x, y

class Camera(GameObject):
    """ object to save the offset of the objects' position when rendering """
    def render(self, surface, gameObjects):
        # print(gameObjects[1].x - self.x)
        for gm in gameObjects:
            gm.render(surface, gm.x - self.x, gm.y - self.y)
        pygame.display.update()

class ColoredRect(GameObject):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
        self.w, self.h = width, height
        self.color = color
    def render(self, surface, x = None, y = None):
        pos = (x or self.x,  y or self.y)
        pygame.draw.rect(surface, self.color, pos + (self.w, self.h))

class Sprite(GameObject):
    def __init__(self, x, y, image):
        self.x, self.y, self.image = x, y, image
    def render(self, surface, x = None, y = None):
        pos = (x or self.x,  y or self.y)
        surface.blit(self.image, pos)

# pygame setup
pygame.init()
SPEED = 500
WIN_WIDTH, WIN_HEIGHT = 800, 800
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# I don't have the old image, so it is replaced by a random image
# the image is to 4 times its original size to cover the whole window
bg_image = pygame.image.load("background.jpg")
# create a game object to represent the image
bg_width, bg_height = bg_image.get_width(), bg_image.get_height()
bg1 = Sprite(0, 0, bg_image)

# set the bounds where the player can move
# the bounds are also used to define the bounds of the camera
# * The bounds can be arbitrary values,
#   but I chose to use the size of the background image.
# * The bounds should be set bigger or equal to the window size
BOUND_RIGHT, BOUND_BOTTOM = max(bg_width, WIN_WIDTH), max(bg_height, WIN_HEIGHT)

# create a game object to represent the player
player = ColoredRect(0, 0, 40, 40, "red")
player_max_x, player_max_y = BOUND_RIGHT - player.w, BOUND_BOTTOM - player.h

# create a game object for testing
coloredRect = ColoredRect(100, 100, 40, 40, "blue")

cam = Camera(-100, -100)
# set the bounds for the camera
cam_max_x, cam_max_y = BOUND_RIGHT - WIN_WIDTH, BOUND_BOTTOM - WIN_WIDTH

# register the game objects for later reference when rendering
gameObjects = [bg1, coloredRect, player] # game objects

# main loop setup
running = True
time_last = pygame.time.get_ticks()

# mainloop
while running:
    # delta time (time passed)
    time = pygame.time.get_ticks()
    dt = (time_last - time) / 1000 # in seconds
    time_last = time

    # handle 'X' button
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    
    # player movements
    motion = [0, 0]
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: motion[1] += SPEED
    if pressed[pygame.K_DOWN]: motion[1] -= SPEED
    if pressed[pygame.K_LEFT]: motion[0] += SPEED
    if pressed[pygame.K_RIGHT]: motion[0] -= SPEED
    player.x += motion[0] * dt
    player.y += motion[1] * dt

    # keep player in bound
    if player.x < 0: player.x = 0
    elif player.x > player_max_x: player.x = player_max_x
    if player.y < 0: player.y = 0
    elif player.y > player_max_y : player.y = player_max_y

    # camera tracking
    cam.x = player.x - (WIN_WIDTH - player.w) / 2
    cam.y = player.y - (WIN_HEIGHT - player.w) / 2

    # keep camera in bound
    # offset by 10 so that you can see the bounds
    min_x, max_x = -10, cam_max_x + 10
    min_y, max_y = -10, cam_max_y + 10
    if cam.x < min_x: cam.x = min_x
    elif cam.x > max_x: cam.x = max_x
    if cam.y < min_y: cam.y = min_y
    elif cam.y > max_y: cam.y = max_y

    window.fill("black")
    cam.render(window, gameObjects)

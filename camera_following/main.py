import pygame

class GameObject:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Camera(GameObject):
    def render(self, surface, gameObjects):
        for gm in gameObjects:
            gm.render(surface, gm.x - self.x, gm.y - self.y)
        # MODIFIED
        pygame.draw.rect(window, "red", (min_x, min_y, bg_width, bg_height), 1)
        print(self.x, self.y)
        pygame.draw.circle(window, "blue", (self.x, self.y), 2)
        # END MODIFIED
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


pygame.init()
SPEED = 500
WIN_WIDTH, WIN_HEIGHT = 800, 800
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# MODIFIED
# the image is not sent to me, so it is replaced by a random image
# scaled the image to 4 times its original size to cover the whole window
# bg_image = pygame.image.load("background.jpg")
bg_image = pygame.transform.scale_by(pygame.image.load("background.jpg"), 4)
# END MODIFIED
bg_width, bg_height = bg_image.get_width(), bg_image.get_height()
bg1 = Sprite(0, 0, bg_image)
# MODIFIED
# bg2 = Sprite(bg_width, 0, bg_image)
# bg3 = Sprite(0, bg_height, bg_image)
# bg4 = Sprite(bg_width, bg_height, bg_image)
# BOUND_RIGHT, BOUND_BOTTOM = bg_width*2, bg_height*2
# END MODIFIED
BOUND_RIGHT, BOUND_BOTTOM = bg_width, bg_height

player = ColoredRect(0, 0, 40, 40, "red")
player_max_x, player_max_y = BOUND_RIGHT - player.w, BOUND_BOTTOM - player.h

cam = Camera(-100, -100)
cam_max_x, cam_max_y = BOUND_RIGHT - WIN_WIDTH, BOUND_BOTTOM - WIN_WIDTH

# MODIFIED
# gameObjects = [bg1, bg2, bg3, bg4, player] # game objects
gameObjects = [bg1, player] # game objects
# END MODIFIED

running = True
time_last = pygame.time.get_ticks()

while running:
    time = pygame.time.get_ticks()
    dt = (time_last - time) / 1000 # in seconds
    time_last = time

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

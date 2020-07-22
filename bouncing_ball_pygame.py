from math import sqrt
import pygame

pygame.init()
window = pygame.display.set_mode((400, 600))

black = (0, 0, 0, 255)
white = (255, 255, 255, 255)

running = True
t_last = 0

y = 20
v = 0
g = 500
rho = 0.75 # coefficient of restitution
tau = 10 # contact time for bounce in millisecond

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = pygame.time.get_ticks()
    dt = (t - t_last)/1000
    t_last = t

    v += g*dt
    y += v*dt + 0.5*g*dt*dt
    if y >= 580:
        pygame.time.wait(tau)
        y = 580
        v *= -rho

    window.fill(black)
    pygame.draw.circle(window, white, (200, int(y)), 20)
    pygame.display.update()

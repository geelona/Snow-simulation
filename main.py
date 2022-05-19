import sys
import pygame
from random import randint

pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()

objects = []
count = 1000
maxSize = 5

for i in range(count):
    x, y = randint(0, WIDTH), randint(0, HEIGHT)
    size = randint(1, maxSize)
    objects.append([x, y, size])


def draw():
    for obj in objects:
        c_x, c_y = obj[0], obj[1]
        c_size = obj[2]
        c = 55 + 200 // maxSize * c_size
        color = (c, c, c)
        pygame.draw.circle(screen, color, (c_x, c_y), c_size)


def main():
    global count
    while 1:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        mx, my = pygame.mouse.get_pos()
        for obj in objects:
            d = ((mx - obj[0]) ** 2 + (my - obj[1]) ** 2) ** 0.5
            if d < 150:
                obj[0] += (obj[0] - mx) * 0.1
                obj[1] += (obj[1] - my) * 0.1
            obj[1] += obj[2]

            if obj[1] - obj[2] > HEIGHT:
                obj[0], obj[1] = randint(0, WIDTH), -randint(10, 100)
        screen.fill((0, 0, 0))
        draw()
        pygame.draw.circle(screen, (155, 155, 255), (mx, my), 150)
        pygame.display.update()
        clock.tick(60)


main()

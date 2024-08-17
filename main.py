import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("platformer")

WIDTH, HEIGHT = 1000, 700
FPS = 60
PLAYER_VEL = 5

# setting up the pygame window(gui)
window = pygame.display.set_mode((WIDTH, HEIGHT))

# creating a class for players


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0

    def move(self, dx, dy):   # function to move the character
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, FPS):
        self.move(self.x_vel, self.y_vel)

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image

# function to draw the background


def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)

    player.draw(window)
    pygame.display.update()  # Update the display after drawing everything


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Green.png")

    player = Player(100, 100, 50, 50)
    # This while loop will make sure our game/frames run 60 times per second (60 fps)
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image, player)

    pygame.quit()
    quit()


# Running the main function
if __name__ == "__main__":
    main(window)

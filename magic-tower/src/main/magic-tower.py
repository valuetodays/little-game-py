#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1 - Import library
import pygame, random, sys, time
import floor

WHITE = (255, 255, 255)  # a few predefined constant colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
LBLUE = (191, 238, 244)

# 2 - Initialize the game
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

TILE_WIDTH = 32
TILE_HEIGHT = 32

# 3 - Load images
icon0 = pygame.image.load("../resources/images/icon0.png")
icon0Width = icon0.get_width()
icon0Height = icon0.get_height()
tileNumberPerLine = icon0Width // TILE_WIDTH
# get a sub-image of an image
tile001 = icon0.subsurface((0, 0), (TILE_WIDTH, TILE_HEIGHT))

floorObj = floor.Floor()
floorObj.display_layer()
floorObj.load_json_layers()

############
# for test
############
current_layer = floorObj.get_layer()
layer_data = current_layer.get_data()
print(layer_data[0][1])

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill((255, 255, 255, 1))
    current_layer = floorObj.get_layer()
    # 6 - draw the screen elements
    # screen.blit(tile001, (0, 0))
    for i in range(current_layer.get_height()):
        for j in range(current_layer.get_width()):
            floorVal = current_layer.get_data()[i][j]
            if floor.is_not_empty_tile(floorVal):
                indexX = floorVal % tileNumberPerLine
                indexY = floorVal // tileNumberPerLine
                titleN = icon0.subsurface((indexX * TILE_WIDTH, indexY * TILE_HEIGHT), (TILE_WIDTH, TILE_HEIGHT))
                screen.blit(titleN, (j * TILE_HEIGHT, i * TILE_WIDTH))

    # pygame.draw.rect(screen, RED, [96, 83, 10, 10], 20)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)

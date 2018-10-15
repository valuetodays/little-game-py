#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1 - Import library
import pygame, random, sys, time
import floor
import constant


TILE_WIDTH = constant.TILE_WIDTH
TILE_HEIGHT = constant.TILE_HEIGHT

class GameView(object):
    """
    game view
    """

    def __init__(self):
        # 2 - Initialize the game
        pygame.init()
        self.screen = pygame.display.set_mode((constant.GAME_WIDTH, constant.GAME_HEIGHT))

        # 3 - Load images
        self.icon0 = pygame.image.load("../resources/images/icon0.png")
        icon0Width = self.icon0.get_width()
        icon0Height = self.icon0.get_height()
        self.tileNumberPerLine = icon0Width // TILE_WIDTH
        # get a sub-image of an image
        tile001 = self.icon0.subsurface((0, 0), (TILE_WIDTH, TILE_HEIGHT))

        self.floorObj = floor.Floor()
        self.floorObj.display_layer()
        self.floorObj.load_json_layers()

    def start(self):
        ############
        # for test
        ############
        current_layer = self.floorObj.get_layer()
        layer_data = current_layer.get_data()
        print(layer_data[0][1])

        # 4 - keep looping through
        while 1:
            # 5 - clear the screen before drawing it again
            self.screen.fill((255, 255, 255, 1))
            current_layer = self.floorObj.get_layer()
            # 6 - draw the screen elements
            # screen.blit(tile001, (0, 0))
            for i in range(current_layer.get_height()):
                for j in range(current_layer.get_width()):
                    floorVal = current_layer.get_data()[i][j]
                    if floor.is_not_empty_tile(floorVal):
                        indexX = floorVal % self.tileNumberPerLine
                        indexY = floorVal // self.tileNumberPerLine
                        titleN = self.icon0.subsurface((indexX * TILE_WIDTH, indexY * TILE_HEIGHT), (TILE_WIDTH, TILE_HEIGHT))
                        self.screen.blit(titleN, (j * TILE_HEIGHT, i * TILE_WIDTH))

            # pygame.draw.rect(screen, RED, [96, 83, 10, 10], 20)
            # 7 - update the screen
            pygame.display.flip()
            # 8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type == pygame.QUIT:
                    # if it is quit the game
                    exit()
        # end of while()
    # end of start()

    def exit(self):
        pygame.quit()
        exit(0)


if __name__ == '__main__':
    gameView = GameView()
    gameView.start()

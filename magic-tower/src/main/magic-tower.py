#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1 - Import library
import pygame, random, sys, time
import os
import tkinter
import tkinter.messagebox
import floor
import constant
import keyutil

TILE_WIDTH = constant.TILE_WIDTH
TILE_HEIGHT = constant.TILE_HEIGHT


class GameView(object):
    """
    game view
    """
    hero_x = 5
    hero_y = 8

    def __init__(self):
        # 2 - Initialize the game
        pygame.init()
        self.screen = pygame.display.set_mode((constant.GAME_WIDTH, constant.GAME_HEIGHT))

        # 3 - Load images
        file_path = os.path.dirname(__file__)
        print(file_path)
        parent_path = os.path.dirname(file_path)
        print(parent_path)
        self.icon0 = pygame.image.load(os.path.join(parent_path, "resources/images/icon0.png"))
        icon0Width = self.icon0.get_width()
        icon0Height = self.icon0.get_height()
        self.tileNumberPerLine = icon0Width // TILE_WIDTH
        # get a sub-image of an image
        tile001 = self.icon0.subsurface((0, 0), (TILE_WIDTH, TILE_HEIGHT))
        self.hero = self.icon0.subsurface((TILE_WIDTH*14, TILE_HEIGHT*12), (TILE_WIDTH, TILE_HEIGHT))

        self.floorObj = floor.Floor()
        self.floorObj.display_layer()
        self.floorObj.load_json_layers()

    def draw_floor(self):
        # draw layers
        self.floorObj.draw_layers(self)
        
    def draw_hero(self):
        self.screen.blit(self.hero, self.get_hero_pos())

    def get_hero_pos(self):
        return (self.hero_x * TILE_HEIGHT, self.hero_y * TILE_WIDTH)

    def is_win(self):
        if self.hero_x == 3 and self.hero_y == 8:
            tkinter.messagebox.showinfo('系统提示', 'Congratulations! you win!')
            self.hero_move_up()

    def hero_move_left(self):
        self.hero_x = self.hero_x - 1

    def hero_move_right(self):
        self.hero_x = self.hero_x + 1

    def hero_move_up(self):
        self.hero_y = self.hero_y - 1

    def hero_move_down(self):
        self.hero_y = self.hero_y + 1

    def start(self):
        ############
        # for test
        ############
        current_layer = self.floorObj.get_layer()
        layer_data = current_layer.get_layer1()
        print(layer_data[0][1])

        # 4 - keep looping through
        while 1:
            # 5 - clear the screen before drawing it again
            self.screen.fill((255, 255, 255, 1))
            # 6 - draw the screen elements
            # screen.blit(tile001, (0, 0))
            self.draw_floor()
            self.draw_hero()
            self.is_win()

            # pygame.draw.rect(screen, RED, [96, 83, 10, 10], 20)
            # 7 - update the screen
            pygame.display.flip()
            # 8 - loop through the events
            for event in pygame.event.get():
                # check if the event is the X button
                if event.type == pygame.QUIT:
                    # if it is quit the game
                    exit()
                if event.type == pygame.KEYDOWN:
                    if keyutil.is_up(event.key):
                        self.hero_move_up()
                    elif keyutil.is_left(event.key):
                        self.hero_move_left()
                    elif keyutil.is_down(event.key):
                        self.hero_move_down()
                    elif keyutil.is_right(event.key):
                        self.hero_move_right()
        # end of while()
    # end of start()

    def exit(self):
        pygame.quit()
        exit(0)


if __name__ == '__main__':
    gameView = GameView()
    gameView.start()

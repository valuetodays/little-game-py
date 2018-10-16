#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import numpy as np
import json
import os
import constant

TILE_WIDTH = constant.TILE_WIDTH
TILE_HEIGHT = constant.TILE_HEIGHT


class Floor(object):
    """
    Floor class
    """
    layer_dict = {}

    def __init__(self, layer_number=1):
        self.layer_number = layer_number

    def load_json_layers(self):
        if len(self.layer_dict) > 0:
            raise RuntimeError("load_json_layers() can be called only once")
            return

        file_path = os.path.dirname(__file__)
        print(file_path)
        parent_path = os.path.dirname(file_path)
        print(parent_path)
        json_file_dir = os.path.join(parent_path, "resources/floor")
        # json_file_dir = r'C:\Users\Administrator\Desktop\g-resources'
        # json_file_dir = r'C:\Users\billu001\Desktop\g'
        if not os.path.exists(json_file_dir):
            raise FileNotFoundError

        files = os.listdir(json_file_dir)
        # 查出json_file_dir目录下的所有.json文件，并把它们解析成LayerEntity对象，赋值给layer_arr
        for filename in [x for x in files if x.endswith(".json")]:
            self.layer_dict[filename] = self.load_json_file(os.path.join(json_file_dir, filename))

    def load_json_file(self, json_file_path):
        with open(json_file_path, 'r', encoding='utf8') as f:
            json_obj = json.loads(f.read())
            return LayerEntity(json_obj)
    
    def get_layer(self):
        return self.layer_dict[str(self.layer_number) + '.json']

    def get_layer_number(self):
        return self.layer_number

    def display_layer(self):
        print(self.get_layer_number())

    def change_layer_to(self, floor_layer):
        self.layer_number = floor_layer

    def draw_layer(self, layer_number_to_draw, game_view):
        current_layer = self.get_layer()
        for i in range(current_layer.get_height()):
            for j in range(current_layer.get_width()):
                floor_value = -1
                if layer_number_to_draw == 1:
                    floor_value = current_layer.get_layer1()[i][j]
                else:
                    floor_value = current_layer.get_layer2()[i][j]
                if is_not_empty_tile(floor_value):
                    index_x = floor_value % game_view.tileNumberPerLine
                    index_y = floor_value // game_view.tileNumberPerLine
                    title_n = game_view.icon0.subsurface(
                        (index_x * TILE_WIDTH, index_y * TILE_HEIGHT), (TILE_WIDTH, TILE_HEIGHT))
                    game_view.screen.blit(title_n, (j * TILE_HEIGHT, i * TILE_WIDTH))

    def draw_layers(self, game_view):
        self.draw_layer(1, game_view)
        self.draw_layer(2, game_view)

class LayerEntity(object):
    width = 0
    height = 0
    layer1 = None
    layer2 = None

    def __init__(self, json_data_all):
        # we only need first layers
        self.width = int(json_data_all['width'])
        self.height = int(json_data_all['height'])
        json_data_layers = json_data_all['layers']
        self.layer1 = self.parse_layer(json_data_layers[0])
        self.layer2 = self.parse_layer(json_data_layers[1])

    def parse_layer(self, json_data):
        layer_data = [[0 for j in range(self.width)] for i in range(self.height)]

        data_list = json_data['data']
        for i in range(self.height):
            for j in range(self.width):
                layer_data[i][j] = data_list[i * self.width + j] - 1
        return layer_data

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_layer1(self):
        return self.layer1

    def get_layer2(self):
        return self.layer2

    def display(self):
        print("width=", self.get_width(), "height=", self.get_height())
        print("layer1:")
        for i in range(self.height):
            for j in range(self.width):
                print(self.get_layer1()[i][j], end=' ')
            print('')

        print("layer2:")
        for i in range(self.height):
            for j in range(self.width):
                print(self.get_layer2()[i][j], end=' ')
            print('')


def is_empty_tile(tile_value):
    empty_value = -1
    return empty_value == tile_value


def is_not_empty_tile(tile_value):
    return not is_empty_tile(tile_value)


if __name__ == '__main__':
    floor = Floor()
    floor.load_json_layers()
    layer = floor.get_layer()
    layer.display()

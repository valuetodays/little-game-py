#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import numpy as np
import json
import os


class Floor(object):
    """
    Floor class
    """
    layer_dict = {}

    def __init__(self, layer_number=1):
        self.layer_number = layer_number

    def load_json_layers(self):
        json_file_dir = r'C:\Users\Administrator\Desktop\g-resources'
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


class LayerEntity(object):
    width = 0
    height = 0
    data = None
    
    def __init__(self, json_data_all):
        # we only need first layers
        json_data = json_data_all['layers'][0]
        self.width = int(json_data['width'])
        self.height = int(json_data['height'])
        self.data = [[0 for j in range(self.width)] for i in range(self.height)]

        data_list = json_data['data']
        for i in range(self.height):
            for j in range(self.width):
                self.data[i][j] = data_list[i * self.width + j] - 1

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_data(self):
        return self.data


def is_empty_tile(tile_value):
    empty_value = -1
    return empty_value == tile_value


def is_not_empty_tile(tile_value):
    return not is_empty_tile(tile_value)


if __name__ == '__main__':
    floor = Floor()
    floor.load_json_layers()
    print(floor.get_layer())

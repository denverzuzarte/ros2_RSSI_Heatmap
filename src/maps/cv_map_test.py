#!/usr/bin/python3

import cv2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  # noqa: E402
import yaml
import numpy as np
import os

def show_map(map_img):
    print("Show Map func")
    plt.imshow(map_img)
    plt.axis('off')
    plt.title('Waypoints (green=valid, red=too close to obstacle)')
    plt.show()

def run(collision_range = 4, density = 6):
    print("run")
    yaml_path = 'map.yaml'
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)

    origin = data['origin']
    resolution = data['resolution']

    image_path = data['image']
    if not os.path.isabs(image_path):
        image_path = os.path.join(os.path.dirname(yaml_path), image_path)

    map = cv2.imread(image_path)
    if map is None:
        raise FileNotFoundError(f'Map image not found: {image_path}')

    img_grey = cv2.cvtColor(map, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Binary image', img_grey)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(len(map))
    print(len(map[0]))

    _, img_tresh = cv2.threshold(img_grey, 230, 255, cv2.THRESH_BINARY) 
    cv2.imshow('Binary image', img_tresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*collision_range+1, 2*collision_range+1))
    img_erosion = cv2.erode(img_tresh, kernel, iterations=1)

    cv2.imshow('eroded image', img_erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #show_map(img_erosion);

    img_rgb_canvas = cv2.cvtColor(img_erosion, cv2.COLOR_GRAY2BGR)

    for y in range(0, len(map), density):
        for x in range(0, len(map[0]), density):
            if(img_rgb_canvas[y, x][0]):
                img_rgb_canvas[y, x] = (0, 255, 0)

    cv2.imshow('eroded image', img_rgb_canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    show_map(img_rgb_canvas);
    
run()

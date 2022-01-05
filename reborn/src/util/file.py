import os

from reborn.config import IMG_BASE_DIR


def get_imgs():
    imgs = [IMG_BASE_DIR+"/"+file for file in os.listdir(IMG_BASE_DIR)]
    return imgs

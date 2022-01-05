from random import randint


def random_img(img_list: list):
    img_list_len = len(img_list)
    index = randint(0, img_list_len - 1)
    return img_list.pop(index)

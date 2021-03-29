# -*- coding: utf-8 -*-
# data augmentation

import os
import glob
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, array_to_img


def draw_images(generator, x, dir_name, index, exp_num):
    save_name = 'ext_' + str(index)
    g = generator.flow(x, batch_size=1, save_to_dir=dir_name,
                       save_prefix=save_name)
    for i in range(exp_num):
        bach = g.next()


def expansion(train_path, test_path):
    exp_num = input("何倍に拡張しますか: ")
    exp_num = int(exp_num) - 1
    train = train_path + "/*"
    test = test_path + "/*"
    train_files = glob.glob(train)
    test_files = glob.glob(test)

    generator = ImageDataGenerator(
        rotation_range=90,  # 90°まで回転
        width_shift_range=0.1,  # 水平方向にランダムでシフト
        height_shift_range=0.1,  # 垂直方向にランダムでシフト
        channel_shift_range=50.0,  # 色調をランダム変更
        shear_range=0.39,  # 斜め方向(pi/8まで)に引っ張る
        horizontal_flip=True,  # 垂直方向にランダムで反転
        vertical_flip=True  # 水平方向にランダムで反転
    )

    for i in range(len(train_files)):
        img = load_img(train_files[i])
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        draw_images(generator, x, train_path, i, exp_num)

    for i in range(len(test_files)):
        img = load_img(test_files[i])
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        draw_images(generator, x, test_path, i, exp_num)

    return exp_num

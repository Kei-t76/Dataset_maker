# -*- coding: utf-8 -*-
# get ratio
import os
import shutil
import glob


def ratio(copy_path):
    print("データセットを分ける比率を選択してください")
    data_num = len(os.listdir(copy_path))
    while True:
        train_num = None
        test_num = None
        div_num = input("7:3の場合1, 8:2の場合2を入力してください(半角): ")
        if div_num == str(1):
            print("train:test=7:3で分割します")
            train_num = int(data_num * 0.7)
            test_num = data_num - train_num - 1
            #print("train: ", train_num, "枚", "test: ", test_num, "枚")
            ratio = '7:3'
            return train_num, test_num, ratio
        elif div_num == str(2):
            print("train:test=8:2で分割します")
            train_num = int(data_num * 0.8)
            test_num = data_num - train_num - 1
            #print("train: ", train_num, "枚", "test: ", test_num, "枚")
            ratio = '8:2'
            return train_num, test_num, ratio
        else:
            print("1 or 2を入力してください")


def div_img(copy_path, train_path, test_path, train_num):
    copy_data = copy_path + "/*"
    files = glob.glob(copy_data)
    for i in range(len(files)):
        if i < int(train_num):
            shutil.move(files[i], train_path)
        else:
            shutil.move(files[i], test_path)

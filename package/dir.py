# -*- coding: utf-8 -*-
# make train, test dir
import os
import shutil
import glob


def dir_copy():
    while True:
        DIR_PATH = input("上記のリストから拡張するフォルダ名を選択してください: ")
        name = DIR_PATH
        DIR_PATH = "original_data/" + DIR_PATH
        if os.path.exists(DIR_PATH):
            if os.path.exists(DIR_PATH + "_copy"):
                print("{}_copyはすでに存在しています".format(DIR_PATH))
            else:
                DIR_PATH_COPY = DIR_PATH + "_copy"
                shutil.copytree(DIR_PATH, DIR_PATH_COPY)
                # print("{}_copyを作成しました".format(DIR_PATH))
                copy_path = DIR_PATH + "_copy"
                return DIR_PATH, copy_path, name
        else:
            print("フォルダが存在しません, 再入力してください")


def mk_dir(DIR_PATH):
    print("データセットを作成します")
    os.makedirs("dataset", exist_ok=True)
    os.makedirs("dataset/train", exist_ok=True)
    os.makedirs("dataset/test", exist_ok=True)

    if not os.path.isdir("dataset/train/" + DIR_PATH):
        os.makedirs("dataset/train/" + DIR_PATH)
        train_path = "dataset/train/" + DIR_PATH
    else:
        print("trainの中にファイル", DIR_PATH, "はすでに存在しています")

    if not os.path.isdir("dataset/test/" + DIR_PATH):
        os.makedirs("dataset/test/" + DIR_PATH)
        test_path = "dataset/test/" + DIR_PATH
    else:
        print("testの中にファイル", DIR_PATH, "はすでに存在しています")

    return train_path, test_path


def dlt_dir(copy_path):
    shutil.rmtree(copy_path)
    print("-=-=-=-=-")

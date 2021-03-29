# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np
import glob
import os


def backpaste(copy_path, img_len):
    while True:
        get_back = input("背景を加えますか (y/n): ")
        if get_back == "y":
            while True:
                back_ground = "package/white.png"
                if os.path.exists(back_ground):
                    break
                else:
                    print('背景が存在しません')

            #im1: 背景画像のパス
            #im2: 背景をつける画像フォルダのパス
            im1 = cv2.imread(back_ground)
            im1 = cv2.resize(im1, (img_len, img_len))
            path = copy_path + '/*'
            files = glob.glob(path)

            for file in files:
                im2 = cv2.imread(file)
                #im1をim2の中心に貼り付けるためim1, im2の中心座標を取得
                im1_height, im1_width, _ = im1.shape
                im2_height, im2_width, _ = im2.shape

                #print(im1_height, im1_width, im2_height, im2_width)

                im1_mid_hgt = im1_height / 2
                im1_mid_wdt = im1_width / 2
                im2_mid_hgt = im2_height / 2
                im2_mid_wdt = im2_width / 2

                #貼り付け位置はim1の左上の座標を選択するため, im1が中心となる左上座標を取得

                up_left_hgt = int(im1_mid_hgt - im2_mid_hgt)
                up_left_wdt = int(im1_mid_wdt - im2_mid_wdt)
                # print(up_left_hgt)
                # print(up_left_wdt)

                #貼り付け, 保存
                im1[up_left_hgt:up_left_hgt+im2_height,
                    up_left_wdt:up_left_wdt+im2_width] = im2

                cv2.imwrite(file, im1)
                done = 'done'
            return done

        elif get_back == "n":
            didnt = 'none'
            return didnt
        else:
            print("y or n を選択してください")

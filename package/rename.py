# -*- coding: utf-8 -*-
# rename
import glob
import os


def rename(dir_path, copy_path, name):
    while True:
        new_ext = input('統一する拡張子の番号を入力してください(半角), 1:jpg, 2:png: ')
        if new_ext == str(1):
            ext = '.jpg'
            break
        elif new_ext == str(2):
            ext = '.png'
            break
        else:
            print('1 or 2を選択してください(半角)')

    path = copy_path + '/*'
    flist = glob.glob(path)
    org_len = len(flist)
    i = 1
    for file in flist:
        os.rename(file, copy_path + '/' + name + str(i) + ext)
        i += 1
    # print("名前を変更しました")

    return ext, org_len

# -*- coding: utf-8 -*-
import os
import glob
import copy
import pprint
import package.rename
import package.resize_scale
import package.backpaste
import package.get_ratio
import package.dir
import package.expansion


if __name__ == '__main__':
    data_dict = {'ファイル名': 'val0', '元データ数': 'val1', '分割比率': 'val2', '何倍': 'val3',
                 '水増し後train': 'val4', '水増し後test': 'val5', '拡張子': 'val6', '背景': 'val6'}
    data_data = []
    name_path = "original_data"
    files = os.listdir(name_path)
    files_name = [f for f in files if os.path.isdir(
        os.path.join(name_path, f))]

    while True:
        print(files_name)

        DIR_PATH, copy_path, filename = package.dir.dir_copy()
        extension, org_len = package.rename.rename(
            DIR_PATH, copy_path, filename)
        img_len = package.resize_scale.resize(copy_path)
        back = package.backpaste.backpaste(copy_path, img_len)
        train_num, test_num, ratio = package.get_ratio.ratio(copy_path)
        train_path, test_path = package.dir.mk_dir(filename)
        package.get_ratio.div_img(copy_path, train_path,
                                  test_path, train_num)
        package.dir.dlt_dir(copy_path)
        exp_num = package.expansion.expansion(train_path, test_path)

        # データ格納
        data_dict['ファイル名'] = filename
        data_dict['元データ数'] = org_len
        data_dict['分割比率'] = ratio
        data_dict['何倍'] = exp_num + 1
        exp_train_num = train_path + '/*'
        exp_test_num = test_path + '/*'
        train_files = glob.glob(exp_train_num)
        test_files = glob.glob(exp_test_num)
        data_dict['水増し後train'] = len(train_files)
        data_dict['水増し後test'] = len(test_files)
        data_dict['拡張子'] = extension
        data_dict['背景'] = back

        data_data.append(data_dict.copy())
        files_name.remove(filename)
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

        if len(files_name) == 0:
            print("全てのファイルを拡張しました.")
            pprint.pprint(data_data, width=40)
            break

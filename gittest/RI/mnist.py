#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import struct
import numpy as np

"""
gzipファイル(学習用60000個 テスト用10000個)
train-images.idx3-ubyte 学習用画像データ
train-labels.idx1-ubyte 学習用ラベルデータ
t10k-images.idx3-ubyte テスト用画像データ
t10k-labels.idx1-ubyte テスト用ラベルデータ

画像データ(28*28pixel)のフォーマット
先頭16byteがヘッダー(4byte区切りでマジックナンバー,画像枚数,画像高さ,画像幅)
そのあとに28*28=728byte区切りで画像情報

ラベルデータ(識別数は0~9の10種類)のフォーマット
先頭8byteがヘッダー(4byte区切りでマジックナンバー,画像枚数)
そのあとに1byte区切りでラベル情報
"""


images_train_path = os.path.join('data', 'train-images.idx3-ubyte')
labels_train_path = os.path.join('data', 'train-labels.idx1-ubyte')
images_test_path = os.path.join('data', 't10k-images.idx3-ubyte')
labels_test_path = os.path.join('data', 't10k-labels.idx1-ubyte')


def getImages(fpath):
    #rbはバイナリファイルの読み込み
    with open(fpath,'rb') as fI:
        #seekで5byte目にファイルポインタを移す(マジックナンバーを飛ばす)
        fI.seek(4)
        
        #struct.unpack()はバイナリをどのようなデータ型に変換するか
        #'>i'はビッグエンディアンのバイトオーダでint型に変換
        #readで4byteごとに読み込んで文字列として返す(画像枚数,画像高さ,画像幅)
        num = struct.unpack('>i',fI.read(4))[0] 
        rows = struct.unpack('>i',fI.read(4))[0] 
        cols = struct.unpack('>i',fI.read(4))[0]

        nPixels = rows*cols

        #読み込んだデータを1次元配列に格納しサイズを変更し,値を正規化する
        images = np.fromfile(fI, np.uint8).reshape(num, nPixels)
        images = images / 255.0

        return images


def getLabels(fpath):
    with open(fpath,'rb') as fL:
        fL.seek(4)
        num = struct.unpack('>i',fL.read(4))[0]        
        labels = np.fromfile(fL, np.uint8)
            
        return labels


train_images = getImages(images_train_path)
train_labels = getLabels(labels_train_path)
test_images = getImages(images_test_path)
test_labels = getLabels(labels_test_path)

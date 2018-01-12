#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import os
import sys
import re
import numpy as np
import matplotlib as plt

f = urllib2.urlopen('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

    #行ごとに分けて配列にする
    #table = ['5.1,3.5,1.4,0.2,Iris-setosa', '4.9,3.0,1.4,0.2,Iris-setosa', ..]
table = f.read().split() 

sl = np.array([])
sw = np.array([])
pl = np.array([])
pw = np.array([])
labels = np.array([])
features = np.array([])

for i in range(len(table)):
    #行ごとにカンマで区切りfloat型に変換し特徴ごとの配列に追加していく
    sl = np.append(sl,float(table[i].split(',')[0])) 
    sw = np.append(sw,float(table[i].split(',')[1]))
    pl = np.append(pl,float(table[i].split(',')[2]))
    pw = np.append(pw,float(table[i].split(',')[3]))
        
    #labelsを配列に追加していき文字列を数値に変換する
    labels = np.append(labels,table[i].split(',')[4])
    for j in range(len(labels)):
        if labels[j] == 'Iris-setosa':
            labels[j] = 0
        elif labels[j] == 'Iris-versicolor':
            labels[j] = 1
        elif labels[j] == 'Iris-virginica':
            labels[j] = 2

                
#特徴量のデータをまとめる(shape=150*4)
features = np.c_[sl, sw, pl, pw]
#f.close()

#２点間のユークリッド距離を計算
def dist(p0, p1):
    return np.sum((p0 - p1) ** 2)

#k近傍のleaveoneout法
def leave_one_out(features, labels, k):
    accuracy = 0.0
    for i in range(len(features)):
        #ブール型で全て1の配列を生成
        train_features = np.ones(len(features), bool)
        #i番目のパターンをテスト用にする
        train_features[i] = False
        #i番目のみ1, それ以外は0のブール型配列生成
        test_features = ~train_features
        if labels[test_features][0] == predict(features[test_features], features[train_features], k, labels):
            accuracy += 1.0
    #accuracy /= len(features)
    return accuracy
            
def predict(test_data, train_data, k, labels):
    #テストデータと、ある1つの訓練データのユークリッド計算していきarray配列にする
    dists = np.array([dist(train_data[i], test_data)
                          for i in range(len(train_data))])
    #ユークリッド距離のarray配列の昇順のindexを取得(最小のindexは0)
    argdists = dists.argsort()

    setosa_count = 0
    versicolor_count = 0
    virginica_count = 0

    for i in range(len(argdists)):
        for j in range(k):
            if argdists[i] == j:
                if labels[i] == 0:
                    setosa_count += 1
                elif labels[i] == 1:
                    versicolor_count += 1
                else:
                    virginica_count += 1

    count_list = np.array([setosa_count, versicolor_count, virginica_count])

    if count_list[np.argmax(count_list)] == setosa_count:
        return 0
    elif count_list[np.argmax(count_list)] == versicolor_count:
        return 1
    else:
        return 2

print leave_one_out(features, labels, 1)
f.close()

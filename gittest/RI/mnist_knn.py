#!/usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mnist import train_labels,train_images,test_labels,test_images

#２点間のユークリッド距離を計算
def dist(p0, p1):
    return np.sum((p0 - p1) ** 2)


def acc(test_data, train_data, k, test_labels, train_labels):
    accuracy = 0.0
    for i in range(len(test_labels)):
        test_bool = np.zeros(len(test_labels), bool)
        test_bool[i] = True
        
        if np.argmax(test_labels[i]) == predict(test_data[test_bool][0], train_data, k, train_labels):
            accuracy += 1.0
    accuracy = 100 * accuracy / len(test_labels)
    return accuracy


def predict(test_data, train_data, k, train_labels):
    dists = np.array([dist(p, test_data) for p in train_data])
    argdists = dists.argsort()
    count_list = np.zeros(10)

    for i in range(k):
        for j in range(10):
            if train_labels[argdists[i]][j] == 1:
                count_list[j] += 1

    return np.argmax(count_list)


def main():
    k = 5
    train_num = 60000
    test_num = 10000
    train_index = np.random.choice(len(train_images), train_num, replace=False)
    test_index = np.random.choice(len(test_images), test_num, replace=False)
    train_im = np.array([train_images[n] for n in train_index])
    test_im = np.array([test_images[n] for n in test_index])
    train_la = np.array([train_labels[n] for n in train_index])
    test_la = np.array([test_labels[n] for n in test_index])
    accuracy = acc(test_im, train_im, k, test_la, train_la)
    print("k={}, accuracy={}, 訓練データ数={}, テストデータ数={}".format(k,accuracy,train_num,test_num))


if __name__ == "__main__":
    main()

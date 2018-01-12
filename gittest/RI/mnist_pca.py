#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import random
from mnist import train_labels,train_images,test_labels,test_images
import matplotlib.pyplot as plt

def pca(data, dim):
    data_bar=np.array([row-np.mean(row) for row in data.T]).T
    m = np.dot(data_bar.T,data_bar)/data.shape[0]
    w,v=np.linalg.eig(m)
    v=v.T
    tmp={}
    for i,value in enumerate(w):
        tmp[value]=i
    v_sorted=[]
    for key in sorted(tmp.keys(),reverse=True):
        v_sorted.append(v[tmp[key]])
    v_sorted=np.array(v_sorted)
    w_sorted=np.array(sorted(w,reverse=True))
    pca=np.dot(data_bar,v_sorted[:dim,].T)
    return pca

#２点間のユークリッド距離を計算
def dist(p0, p1):
    return np.sum((p0 - p1) ** 2)

train_num = 300
test_num = 50
train_index = np.random.choice(len(train_images), train_num, replace=False)
test_index = np.random.choice(len(test_images), test_num, replace=False)
train_im = np.array([train_images[n] for n in train_index])
test_im = np.array([test_images[n] for n in test_index])
train_la = np.array([train_labels[n] for n in train_index])

pca = pca(train_im, 2)

data0 = np.array([x for i,x in enumerate(pca) if train_la[i][0] == 1])
data1 = np.array([x for i,x in enumerate(pca) if train_la[i][1] == 1])
data2 = np.array([x for i,x in enumerate(pca) if train_la[i][2] == 1])
data3 = np.array([x for i,x in enumerate(pca) if train_la[i][3] == 1])
data4 = np.array([x for i,x in enumerate(pca) if train_la[i][4] == 1])
data5 = np.array([x for i,x in enumerate(pca) if train_la[i][5] == 1])
data6 = np.array([x for i,x in enumerate(pca) if train_la[i][6] == 1])
data7 = np.array([x for i,x in enumerate(pca) if train_la[i][7] == 1])
data8 = np.array([x for i,x in enumerate(pca) if train_la[i][8] == 1])
data9 = np.array([x for i,x in enumerate(pca) if train_la[i][9] == 1])
dataset = np.array([data0,data1,data2,data3,data4,data5,data6,data7,data8,data9])
colors = [plt.cm.hsv(0.1*i, 1) for i in range(10)]

def near(vector, center_vectors):
    euclid_dist = lambda vector1, vector2: (sum([(vec[0]-vec[1])**2 for vec in list(zip(vector1, vector2))]))**0.5
    d = [euclid_dist(vector, center_vector) for center_vector in center_vectors]
    return d.index(min(d))

def clustering(vectors, label_count, learning_count_max=1000):
    #各vectorに割り当てられたクラスタラベルを保持するvector
    label_vector = [random.randint(0, label_count-1) for i in vectors]
    #一つ前のStepで割り当てられたラベル。終了条件の判定に使用
    old_label_vector = list()
    #各クラスタの重心vector
    center_vectors = [[0 for i in range(len(vectors[0]))] for label in range(label_count)]

    for step in range(learning_count_max):
        #各クラスタの重心vectorの作成
        for vec, label in zip(vectors, label_vector):
            center_vectors[label] = [c+v for c, v in zip(center_vectors[label], vec)]
        for i, center_vector in enumerate(center_vectors):
            center_vectors[i] = [v/label_vector.count(i) for v in center_vector]
        #各ベクトルのラベルの再割当て
        for i, vec in enumerate(vectors):
            label_vector[i] = near(vec, center_vectors)
        #前Stepと比較し、ラベルの割り当てに変化が無かったら終了
        if old_label_vector == label_vector:
            break
        #ラベルのベクトルを保持
        old_label_vector = [l for l in label_vector]
    return center_vectors


centers=clustering(pca,10)
labels = np.zeros(len(pca))
for i in range(len(pca)):
    labels[i] = near(pca[i],centers)
    
plt.subplot(121)
for i in range(10):
    plt.scatter(dataset[i][:,0],dataset[i][:,1], alpha=0.6, c=colors[i], label=str(i))
plt.legend()
plt.title("PCA of MNIST")

plt.subplot(122)
for i in range(len(pca)):
    plt.scatter(pca[i][0],pca[i][1], alpha=0.6, c=colors[int(labels[i])], label=str(labels[i]))
plt.title("kmeans of MNIST")
plt.show()

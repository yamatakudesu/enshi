#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from mnist import train_labels, train_images, test_labels, test_images
from function import softmax


#10クラス分類でクラス2の教師信号なら[0,1,0,0,0,0,0,0,0,0]となる
def one_of_k(data):
    labels = np.zeros((len(data), 10))
    for i in range(len(data)):
        labels[i][data[i]] = 1
        
    return labels


train_labels = one_of_k(train_labels)
test_labels = one_of_k(test_labels)

w = np.random.normal(0, 0.1, (784, 10))
learning_rate = 0.01

for x, t in zip(train_images, train_labels):
    p = softmax(np.dot(w.T, x))
    x = np.reshape(x, (784, 1))
    q = np.reshape(p.T - t, (1, 10))
    w -= learning_rate * np.dot(x, q)

acc = 0.0
for x, t in zip(test_images, test_labels):
    p = softmax(np.dot(w.T, x))
    if t[np.argmax(p)] == 1:
        acc += 1.0
acc /= len(test_images)
        
print(acc)

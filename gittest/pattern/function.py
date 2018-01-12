#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import random

class Net():
    def __init__(self, neurons):
        #neuronsは層ごとのneuron数を配列に格納したもの
        #ThreeLayerNet([2,4,3])なら3層でneurons数が入力層から順に2個4個3個
        self.neurons = neurons

        #layer数
        self.layers = len(neurons)

        #bias(標準正規分布による1*pの行列)
        self.b = [np.random.randn(1, neurons[i])
                  for i in range(1, self.layers)]

        #weight        
        self.w = [np.random.randn(neurons[i-1], neurons[i])
                  for i in range(1, self.layers)]


    def feedforward(self, x):
        z = np.array([])
        u = np.array([])
        z = np.append(z, x)

        b = self.b
        w = self.w
        L = self.layers

        #出力層以外の活性化関数をsigmoid
        for l in range(1, L-1):
            u = np.append(u, np.dot(w[l].T, z[l-1]) + b[l])
            z = np.append(z, sigmoid(u[l-1]))

        #出力層での活性化関数をsoftmax
        u = np.append(u, np.dot(w[L].T, z[L-1]) + b[L]) 
        z = np.append(z, softmax(u[L-1]))
        
        return z[L]


 






def identity_function(x):
    return x


def step_function(x):
    return np.array(x > 0, dtype=np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))    


def sigmoid_grad(x):
    return (1.0 - sigmoid(x)) * sigmoid(x)
    

def relu(x):
    return np.maximum(0, x)


def relu_grad(x):
    grad = np.zeros(x)
    grad[x>=0] = 1
    return grad
    

def softmax(x):
    if x.ndim == 2:
        x = x.T
        x = x - np.max(x, axis=0)
        y = np.exp(x) / np.sum(np.exp(x), axis=0)
        return y.T 

    x = x - np.max(x) # オーバーフロー対策
    return np.exp(x) / np.sum(np.exp(x))


def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)


def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    # 教師データがone-hot-vectorの場合、正解ラベルのインデックスに変換
    if t.size == y.size:
        t = t.argmax(axis=1)
             
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t])) / batch_size


def softmax_loss(X, t):
    y = softmax(X)
    return cross_entropy_error(y, t)


    

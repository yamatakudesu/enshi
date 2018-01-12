#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import random
from mnist import train_labels,train_images,test_labels,test_images
from function import relu, softmax
import matplotlib.pyplot as plt

class Net():
    def __init__(self, neurons):
        #neuronsは層ごとのneuron数を配列に格納したもの
        #Net([784,100,10])なら3層でneurons数が順に784個100個10個のユニット
        self.neurons = neurons

        #layer数
        self.layers = len(neurons)

        #bias(正規分布によるサイズneurons[i]の行列をlayer-1個配列に格納)
        self.B = [np.random.normal(0,0.1,neurons[i])
                  for i in range(1, self.layers)]

        #weight(正規分布によるneurons[i-1]*neurons[i]の行列をlayer-1個)      
        self.W = [np.random.normal(0,0.1,(neurons[i-1], neurons[i]))
                  for i in range(1, self.layers)]
        
        
    #順伝播
    def forprop(self, x):
        #input:入力層ユニット(mnistなら大きさ784の配列)
        #output:活性化前後のデータをlayer数まとめたもの
        B = self.B
        W = self.W
        L = self.layers
        Z = [np.array([]) for l in range(L)]
        U = [np.array([]) for l in range(L)]
        Z[0] = x

        #出力層以外の活性化関数をrelu
        for l in range(1, L-1):
            U[l-1] = np.dot(W[l-1].T, Z[l-1]) + B[l-1]
            Z[l] = relu(U[l-1])
            
        #出力層での活性化関数をsoftmax
        U[L-2] = np.dot(W[L-2].T, Z[L-2]) + B[L-2]
        Z[L-1] = softmax(U[L-2])
        
        return U, Z


    #逆伝播
    def backprop(self, Z, t, dB, dW):
        #input Z: 活性化されたデータをまとめたもの
        #input t: one-of-k化されたラベルデータ
        #input dB, dW: biasとweightの誤差
        #output: 更新後のbiasとweightの誤差
        W = self.W
        L = self.layers
        neurons = self.neurons

        delta = [np.zeros(neurons[l+1]) for l in range(L-1)]
        delta[L-2] = Z[L-1] - t

        for l in range(L-2, 0, -1):
            delta[l-1] = Z[l] * np.dot(W[l], delta[l])
            dB[l-1] += delta[l-1]
            dW[l-1] += np.dot(Z[l-1].reshape(len(Z[l-1]),1),delta[l-1].reshape(len(delta[l-1]),1).T)

        return dB, dW

    
    #bias, weightの更新
    def update(self, noise=0):
        global train_images, test_images, train_labels, test_labels
        #output: 更新後のbias, weight
        B = self.B
        W = self.W
        L = self.layers
        neurons = self.neurons

        #バッチサイズ
        batch_size = 100
        #エポック数
        num_epoch = 30

        count = 0
        acc_list = np.array([])

        ###noise version###
        if noise != 0:
            train_images = self.noise(train_images, noise)
            test_images = self.noise(test_images, noise)
        ###################
        
        for m in range(int(len(train_images)/batch_size*num_epoch)):

            #学習係数
            if m < int(len(train_images)/batch_size*5):
                learning_rate = 0.08
            elif m < int(len(train_images)/batch_size*10):
                learning_rate = 0.05
            elif m < int(len(train_images)/batch_size*15):
                learning_rate = 0.01
            else:
                learning_rate = 0.005
                
            dB = [np.zeros(neurons[i+1]) for i in range(L-1)]
            dW = [np.zeros((neurons[i],neurons[i+1]))
                  for i in range(L-1)]
            
            #ランダムにミニバッチに選ばれた訓練データbatch_size個のindex(重複なし)
            index = np.random.choice(len(train_images), batch_size, replace=False)

            #ミニバッチデータ(mnistなら784のデータがbatch_size個)
            minibatch = [train_images[n] for n in index]

            for i in range(batch_size):
                Z = [np.array([]) for l in range(L)]
                U = [np.array([]) for l in range(L)]
                Z[0] = minibatch[i]
                #順伝播
                U, Z = self.forprop(Z[0])
                #誤差逆伝播
                dB, dW = self.backprop(Z,train_labels[index[i]],dB,dW)

            #bias, weightの更新
            for l in range(L-1):
                B[l] -= learning_rate / batch_size * dB[l]
                W[l] -= learning_rate / batch_size * dW[l]

            #epochごとに識別率を表示
            if m % (len(train_images)/batch_size) == 0:
                accuracy = self.predict(B,W,test_images,test_labels)                
                acc_list = np.append(acc_list, accuracy)
                print("epoch:{} accuracy:{}%".format(count, accuracy))
                count += 1
     
        return B, W, acc_list, count
    
   
    def predict(self,B,W,X_test,Y_test):
        #input: bias, weight
        #output: 識別率
        L = self.layers
        accuracy = 0.0

        #テストデータの予測が合っているか調べる
        for i in range(len(X_test)):
            U,Z = self.forprop(X_test[i])
            if np.argmax(Z[L-1]) == np.argmax(Y_test[i]):
                accuracy += 1.0

        accuracy = accuracy / len(X_test) * 100

        return accuracy


    def noise(self, data, p):
        #input data: データ
        #input p: ノイズ発生確率[%]
        #output: ノイズが追加されたデータ
        for i in range(len(data)):
            for j in range(len(data[i])):
                if np.random.randint(1, 101) <= p:
                    data[i][j] = np.random.rand()

        return data

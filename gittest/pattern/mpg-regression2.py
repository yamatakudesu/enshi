# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

#data.txtを読み込む
names=["mpg",
       "cylinders",
       "displacement",
       "horsepower",
       "weight",
       "acceleration",
       "year",
       "origin",
       "car name"]
cars=pd.read_csv("./data.txt",delim_whitespace=True,names=names)
#ミスデータ'?'がある部分の除去
cars=cars[cars['horsepower']!='?']
#pandas型からnumpy型に変換
table=np.array(cars)

mpg = np.array([]) #continuous
cylinders = np.array([]) #multi-valued discrete
displacement = np.array([]) #continuous
horsepower = np.array([]) #continuous
weight = np.array([]) #continuous
acceleration = np.array([]) #continuous
year = np.array([]) #multi-valued discrete
origin = np.array([]) #multi-valued discrete
name = np.array([]) #string (unique for each instance)

for i in range(len(table)):
    #行ごとに区切り特徴ごとの配列に追加していく
    #horsepowerにミスデータが存在し文字列配列になっているのでfloat型に変換
    mpg = np.append(mpg,(np.split(table[i],1)[0][0])) 
    cylinders= np.append(cylinders,(np.split(table[i],1)[0][1])) 
    displacement = np.append(displacement,(np.split(table[i],1)[0][2])) 
    horsepower = np.append(horsepower,(float)(np.split(table[i],1)[0][3])) 
    weight = np.append(weight,(np.split(table[i],1)[0][4])) 
    acceleration= np.append(acceleration,(np.split(table[i],1)[0][5])) 
    year = np.append(year,(np.split(table[i],1)[0][6])) 
    origin = np.append(origin,(np.split(table[i],1)[0][7])) 
    name = np.append(name,(np.split(table[i],1)[0][8])) 

def regression2d(x1, x2, y):
    x = np.c_[x1,x2]
    y = np.c_[mpg]
    x0 = np.ones((len(x1),1))
    x = np.c_[x0, x1, x2]
    a = np.dot(x.T, x)
    b = np.linalg.pinv(a)
    c = np.dot(b, x.T)
    w = np.dot(c, y)
    print w
    return (w[0], w[1], w[2])

def regression3d(x1, x2, x3, y):
    x = np.c_[x1,x2,x3]
    y = np.c_[mpg]
    x0 = np.ones((len(x1),1))
    x = np.c_[x0, x1, x2, x3]
    a = np.dot(x.T, x)
    b = np.linalg.pinv(a)
    c = np.dot(b, x.T)
    w = np.dot(c, y)
    print w
    return (w[0], w[1], w[2], w[3])
    
def regression4d(x1, x2, x3, x4, y):
    x = np.c_[x1,x2,x3,x4]
    y = np.c_[mpg]
    x0 = np.ones((len(x1),1))
    x = np.c_[x0, x1, x2, x3,x4]
    a = np.dot(x.T, x)
    b = np.linalg.pinv(a)
    c = np.dot(b, x.T)
    w = np.dot(c, y)
    print w
    return (w[0], w[1], w[2], w[3], w[4])

fig = plt.figure()
fig1 = plt.figure()
fig2 = plt.figure()
x1 = np.arange(0,250,10)
x2 = np.arange(0,5000,200)
X1, X2 = np.meshgrid(x1,x2)

w0, w1, w2=regression2d(horsepower,weight,mpg)
ax = Axes3D(fig)
ax.set_xlim(250,0)
ax.set_ylim(0, 5500)
ax.set_zlim(0, 50)
ax.scatter3D(horsepower,weight,mpg)
ax.plot_wireframe(X1,X2,w0+w1*X1+w2*X2)
ax.set_xlabel("horsepower")
ax.set_ylabel("weight")
ax.set_zlabel("mpg")

w0, w1, w2, w3=regression3d(horsepower,weight,acceleration,mpg)
ax1 = Axes3D(fig1)
ax1.set_xlim(250,0)
ax1.set_ylim(0, 5500)
ax1.set_zlim(0, 50)
ax1.scatter3D(horsepower,weight,mpg)
ax1.plot_wireframe(X1,X2,w0+w1*X1+w2*X2)
ax1.set_xlabel("horsepower")
ax1.set_ylabel("weight")
ax1.set_zlabel("mpg")

w0, w1, w2, w3, w4=regression4d(horsepower,weight,acceleration,displacement,mpg)
ax2 = Axes3D(fig2)
ax2.set_xlim(250,0)
ax2.set_ylim(0, 5500)
ax2.set_zlim(0, 50)
ax2.scatter3D(horsepower,weight,mpg)
ax2.plot_wireframe(X1,X2,w0+w1*X1+w2*X2)
ax2.set_xlabel("horsepower")
ax2.set_ylabel("weight")
ax2.set_zlabel("mpg")

plt.show()

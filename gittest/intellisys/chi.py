# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def chi(ax,k):
    n = 20000
    xx = np.zeros(n)
    #標準正規分布に従う乱数生成
    for i in range(k):
        x = np.random.normal(0, 1, n)
        x2 = x**2
        xx += x2
    #ヒストグラム描画
    ax.set_xlim(0,25)
    ax.set_ylim(0,0.6)
    ax.set_title("k=%d" %(k))
    ax.hist(xx, 80, normed=True) #データ配列、棒の数、正規化
    
def main():
     # 結果表示
    fig = plt.figure(figsize=(18,25))
    for i in range(1,11):
        chi(fig.add_subplot(2,5,i),i)
    plt.show()
    plt.saveimg("chi.png")

if __name__ == '__main__':
    main()

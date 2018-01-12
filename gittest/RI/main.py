#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from network import Net

def main():
    net = Net([784,100,50,10])
    print("neurons: {}".format(net.neurons))
    B, W, acc, count = net.update(noise=0)
    x = np.array([i for i in range(count)])
    y = np.array([acc[i] for i in range(count)])
    plt.plot(x,y)
    plt.xlabel("epoch")
    plt.ylim(50.0, 100.0)
    plt.ylabel("accuracy[%]")
    plt.title("neurons: {}".format(net.neurons))
    plt.show()
    
    
if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
import numpy as np

#連立方程式AX=Bの解を求める
A = np.array([[1.0, 3.0],
              [2.0, 2.0]])

B = np.array([1.0,0.0])


X = np.linalg.solve(A, B)
print(X)

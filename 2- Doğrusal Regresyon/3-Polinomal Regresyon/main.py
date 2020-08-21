#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:16:05 2020

@author: mbulut
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


veriler=pd.read_csv("maaslar.csv")


x=veriler["Egitim Seviyesi"].values.reshape(-1,1)
y=veriler["maas"].values.reshape(-1,1)

### LİNEER YÖNTEM
"""
from sklearn.linear_model import LinearRegression

lr=LinearRegression()

lr.fit(x,y)

y_pred=lr.predict(x)

plt.scatter(x,y,color="orange")
plt.plot(x,y_pred**3,color="green")"""


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=4)
x_poly=poly_reg.fit_transform(x)

lr=LinearRegression()
lr.fit(x_poly,y)


plt.scatter(x,y,color="orange")

y_pred=lr.predict(x_poly)
plt.plot(x,y_pred,color="blue")















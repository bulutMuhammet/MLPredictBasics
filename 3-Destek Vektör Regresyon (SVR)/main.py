#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:44:36 2020

@author: mbulut
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


veriler=pd.read_csv("maaslar.csv")


x=veriler["Egitim Seviyesi"].values.reshape(-1,1)
y=veriler["maas"].values.reshape(-1,1)



#verilerin ölçeklenmesi

from sklearn.preprocessing import StandardScaler

sc1=StandardScaler()
x_olcek=sc1.fit_transform(x)

sc2=StandardScaler()
y_olcek=sc2.fit_transform(y)

from sklearn.svm import SVR

svr_reg=SVR(kernel='rbf')
svr_reg.fit(x_olcek,y_olcek)

plt.scatter(x_olcek,y_olcek,color="red")
plt.plot(x_olcek,svr_reg.predict(x_olcek),color="blue")














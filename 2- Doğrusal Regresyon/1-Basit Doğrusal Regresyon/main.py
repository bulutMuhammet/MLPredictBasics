#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:53:27 2020

@author: mbulut
"""


#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#2. Veri Onisleme

#2.1. Veri Yukleme
veriler = pd.read_csv('satislar.csv')
#pd.read_csv("veriler.csv")


#veri on isleme
aylar = veriler[['Aylar']]
#test
print(aylar)

satislar = veriler[['Satislar']]
print(satislar)


#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.33, random_state=0)
"""
#verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
Y_train=sc.fit_transform(y_train)
Y_test=sc.fit_transform(y_test)
"""
from sklearn.linear_model import LinearRegression

lr=LinearRegression()
lr.fit(x_train,y_train)

predict=lr.predict(x_test)
x_train=x_train.sort_index()
y_train=y_train.sort_index()
plt.scatter(x_train,y_train)
plt.plot(x_test,predict,color="green")
plt.title("Aylara göre satış")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")

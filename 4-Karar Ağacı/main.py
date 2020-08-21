#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:12:35 2020

@author: mbulut
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


veriler=pd.read_csv("maaslar.csv")


x=veriler["Egitim Seviyesi"].values.reshape(-1,1)
y=veriler["maas"].values.reshape(-1,1)


from sklearn.tree import DecisionTreeRegressor

r_dt=DecisionTreeRegressor(random_state=0)
r_dt.fit(x,y)
plt.scatter(x,y,color="red")
plt.plot(x,r_dt.predict(x),color="blue")

print(r_dt.predict([[6.6]]))
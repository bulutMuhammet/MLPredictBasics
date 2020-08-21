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


from sklearn.ensemble import RandomForestRegressor

rf_reg=RandomForestRegressor(n_estimators=10,random_state=0)
rf_reg.fit(x,y)

plt.scatter(x,y,color="red")
plt.plot(x,rf_reg.predict(x),color="blue")

from sklearn.metrics import r2_score

print("Random Forest R2 degeri")
print(r2_score(y,rf_reg.predict(x)))
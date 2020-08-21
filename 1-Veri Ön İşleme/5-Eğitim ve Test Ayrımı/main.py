#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:59:31 2020

@author: mbulut
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("veriler.csv")

ulke=df.iloc[:,0:1]

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
ulke.iloc[:,0]=le.fit_transform(ulke.iloc[:,0])

ohe=OneHotEncoder(categories="auto")
ulke=ohe.fit_transform(ulke).toarray()

sonuc=pd.DataFrame(data=ulke,index=range(22),columns=['fr','tr','us'])


df["yas"] = df["yas"].fillna(df["yas"].mean())

sonuc2=pd.DataFrame(data=df,index=range(22),columns=['boy','kilo','yas'])


cinsiyet=df.iloc[:,-1].values

sonuc3=pd.DataFrame(data=cinsiyet,index=range(22),columns=['cinsiyet'])

s=pd.concat([sonuc,sonuc2],axis=1)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test=train_test_split(s,sonuc3,test_size=0.33,random_state=42)
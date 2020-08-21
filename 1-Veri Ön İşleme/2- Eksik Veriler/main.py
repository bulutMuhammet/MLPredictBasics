#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 19:11:58 2020

@author: mbulut
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("veriler.csv")


df["yas"] = df["yas"].fillna(df["yas"].mean())

"""
from sklearn.impute import SimpleImputer
 
imputer = SimpleImputer(missing_values=np.nan, strategy = 'mean')
 
Yas = veriler.iloc[:,1:4].values     #iloc pandas kütüphanesinde hangi kolonları almamızı belirlediğimiz fonk.
print(Yas)
 
 
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas) 

"""
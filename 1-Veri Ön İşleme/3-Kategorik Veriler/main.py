#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:58:14 2020

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
ulkedf=pd.DataFrame(ulke)
ulkedf.columns=['France','Turkey','USA']
del df["ulke"]
df=pd.concat([ulkedf,df],axis=1)
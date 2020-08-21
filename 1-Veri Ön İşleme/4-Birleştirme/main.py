#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:48:03 2020

@author: mbulut
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("veriler.csv")

"""
Daha önceki kodlarda ayrılan, kesilen, biçilen veriler aşağıdaki gibi birleştirilir.

sonuc=pd.DataFrame(data=ulke,index=range(22),columns=['fr','tr','us'])
print(sonuc)

sonuc2=pd.DataFrame(data=Yas,index=range(22),columns=['boy','kilo','yas'])

print(sonuc)

s=pd.concat([sonuc,sonuc2],axis=1)

"""
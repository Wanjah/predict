# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:50:50 2021

@author: admin
"""
#importing library
import pandas as pd

#importing dataset
headers=["Beverages","Carbs","Proteins","Vitamins","Description"]
dset = pd.read_csv("other.csv",header=None,names=headers,na_values="?")

X= dset.iloc[:,:-1].values

#Encoding categorical data
from sklearn.preprocessing import OrdinalEncoder
enc=OrdinalEncoder()
enc.fit(X)
X=enc.transform(X)
#Encoding target data
y=dset.iloc[:,-1]
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
le.fit(y)
y=le.transform(y)

import random
i=enc.inverse_transform(X)
for n in i:
        tuple(i)
        print("Your meals for the day:")
        print("Breakfast:",i[random.getrandbits(4)],'\n',"lunch:",i[random.getrandbits(3)],'\n',"Supper:",i[random.getrandbits(3)])
        break

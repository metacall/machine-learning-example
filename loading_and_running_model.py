#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: akash.joshi
"""

# Importing the libraries
#import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd
from joblib import dump,load

regressor = load('model.joblib')

# Importing the dataset
'''dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)'''

# Loading model in memory
def predict_salary(input):
    return regressor.predict(input)

#Visualization of Training Set
'''plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Sal vs Exp (Training Set)')
plt.xlabel('Yrs of Exp')
plt.ylabel('Salary')
plt.show()

#Visualization of Test Set
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Sal vs Exp (Test Set)')
plt.xlabel('Yrs of Exp')
plt.ylabel('Salary')
plt.show()'''
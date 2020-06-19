#!/usr/bin/python3

# Model by: https://github.com/akash-joshi
import pickle
import os

# Read model file
basepath = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(basepath, 'model.sav'), 'rb') as f:
  regressor = pickle.load(f)

def predict_salary(input):
	return regressor.predict(input).tolist()

# print(predict_salary([[10], [20]]))

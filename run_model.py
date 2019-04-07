#!/usr/bin/python3

# Model by: https://github.com/akash-joshi/metacall-ml-example
import pickle
import os

current_path = os.path.dirname(os.path.realpath(__file__))

regressor = pickle.load(open('model.sav','rb'))

def predict_salary(input):
	return regressor.predict(input).tolist()

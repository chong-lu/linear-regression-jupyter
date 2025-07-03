#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using Python to model Salary based on Years of Experience.
import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress
if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

data = pd.read_csv(filename)
model = LinearRegression()
model.fit(data[[x_col]], data[[y_col]])
slope, intercept, r_value, p_value, std_err = linregress(data[x_col], data[y_col])
print(f"slope is {slope}, r_value is {r_value}")
plt.scatter(data[[x_col]], data[[y_col]], color='red')
plt.plot(data[[x_col]], model.predict(data[[x_col]]), color='blue', label='Fitted line')
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.text(1.25, 60000, f"y = {slope:.2f}x + {intercept:.2f}\nr = {r_value:.2f}")
plt.savefig("linear_regression_python_output.png")
plt.show()

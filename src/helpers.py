import pandas as pd
import numpy as np

def calculate_five_percent(y_predict,y_test):
    differences = ((np.abs(y_predict - y_test))/y_test) * 100
    differences = ['{:f}'.format(item) for item in differences]
    underfive = []
    overfive = []
    for i in differences:
        i = float(i)
        if i >= 5.0:
            overfive.append(i)
        else:
            underfive.append(i)
    percent_under_five = len(underfive)/len(differences)
    return percent_under_five * 100

def calculate_ten_percent(y_predict,y_test):
    differences = ((np.abs(y_predict - y_test))/y_test) * 100
    differences = ['{:f}'.format(item) for item in differences]
    underten = []
    overten = []
    for i in differences:
        i = float(i)
        if i >= 10.0:
            overten.append(i)
        else:
            underten.append(i)
    percent_under_ten = len(underten)/len(differences)
    return percent_under_ten * 100

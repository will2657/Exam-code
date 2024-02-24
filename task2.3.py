import numpy as np
from numpy import random 
import csv
from IPython.display import display

def randomiser(filename,X,Y):
    TwoDnumpy = np.array(random.randint(100, size=(X,Y)))
    print(TwoDnumpy)
    np.savetxt(filename, TwoDnumpy)
randomiser("will.csv",5,7)  
def fileiser(file):
    arr = np.genfromtxt(file,
    delimiter=",", dtype=str)
    with open(file,'r') as x:
        will = list(csv.reader(x, delimiter=','))
    will = np.array(will)
    display(will)
    counter = 0
    print(will.shape)
    x_lim = will.shape[0]
    y_lim = will.shape[1]

    x = int(input("Add column number please"))
    y = int(input("Add row number please"))
    while (x > x_lim ) or (x < 0):
        x = input("Please input between 0 and", str(x_lim))
    while (y > y_lim ) or (y < 0):
        y = input("Please input between 0 and", str(y_lim))
    print("This is yada yada",str(will[x][y]))
    for array in will :
        for item in array:
            counter += 1
            print("Elemnt number", str(counter),  "is",str(item))
            
fileiser("will.csv")
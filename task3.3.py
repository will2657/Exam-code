import matplotlib.pyplot as plt
import numpy as np
import random 

def barchart(array):
    x_values = np.arange(0,len(array),1).astype(str)
    plt.bar(x_values,array,color='blue')
    plt.title('array cell number')
    plt.ylabel('array cell value')
    plt.show()
randomlength=np.random.randint(1,10)    
randomarray=np.random.randint(10,size=(randomlength))
barchart(randomarray)
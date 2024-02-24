import numpy as np

arr = np.array([[[4, 5, 6],[1, 2, 3]], 
                
                [[14, 15, 16],[11, 12, 13]], 
                
                [[24, 25, 26],[21, 22, 23]]])

print(arr.shape)
for x in np.nditer(arr):
    print(x)
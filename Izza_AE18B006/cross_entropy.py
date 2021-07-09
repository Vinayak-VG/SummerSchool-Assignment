import numpy as np
y = np.random.randint(0,2,(100))
y_cap = np.random.random_sample(size= 100)
O = (-1/100)* np.sum((y * np.log2(y_cap) + (1-y)*np.log2(1-y_cap)))

print(O)
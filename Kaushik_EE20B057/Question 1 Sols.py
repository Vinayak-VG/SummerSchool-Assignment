import numpy as np
import math as mt
y_cap = np.random.rand(100,)
y = np.random.randint(0,2,(100,))
a_arr = np.log(y_cap)/mt.log(2)
b_arr = np.log(1-y_cap)/mt.log(2)
O_arr = (-1/100)*((y*a_arr) + ((1-y)*b_arr))
O = np.sum(O_arr)
print(O)
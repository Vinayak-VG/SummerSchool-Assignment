#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

try:
    n = int(input('enter value of n'))
except:
    n= 100
y_cap = np.random.rand(n,)
y = np.random.randint(0,2,(n,))
o = 0

for i in range(0,n,1):
    o = o + y[i]*np.log2(y_cap[i]) + (1-y[ihttp://localhost:8888/notebooks/me19b053.1.ipynb#])*np.log2(1-y_cap[i])
o = ((-1)/n)*o
print(o)


# In[ ]:





# In[ ]:





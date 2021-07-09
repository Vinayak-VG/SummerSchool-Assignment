# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 09:58:16 2021

@author: CIBI
"""

import numpy as np
from numpy import random

y1=random.rand(100)
a=random.randint(2,size=(100))
y=a.astype(float)

y2=np.subtract(1,y1)
logy1=np.log2(y2)
logy=np.log2(y1)

new1=np.multiply(y,logy)
new2=np.multiply((1-y),logy1)

out=np.sum([new1,new2])

output=-(out/100)

 


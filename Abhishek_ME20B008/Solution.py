#!/usr/bin/env python
# coding: utf-8

# # Assignment
# 

# Solution to problem 1

# importing modules math and random, and creating two empty lists for y and y_hat. 

# In[1]:


import math
import random
n=10
y=[]
y_hat=[]
O=0


# Assigning random numbers to the lists

# In[2]:


for i in range(0,n,1):
    x_hat=random.random()
    y_hat.append(x_hat)
    x=random.randint(0,1)
    y.append(x)


# In[3]:


y


# In[4]:



y_hat


# Evaluating the expression

# In[5]:



for i in range(0,n,1):
    O=O-1/n*(y[i]*math.log(y_hat[i],2) + (1-y[i])*math.log(1-y_hat[i],2))
    


# Final Answer

# In[6]:


O


# Solution to Problem 2

# In[7]:


class Myclass:
    def __init__(self,listofno,target):
        self.listofno=listofno
        self.target=target
    def process(self):
        key=1
        d={}
        for i in range(0,len(self.listofno),1):
            for j in range(0,len(self.listofno),1):
                if((self.listofno[i]+self.listofno[j])==self.target):
                    d[key]=[i,j]
                    key=key+1
        print(d);             


# Output

# In[8]:


p1=Myclass([10,20,30,40,50,60,70],50)       
p1.process()


# In[ ]:





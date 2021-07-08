#!/usr/bin/env python
# coding: utf-8

# In[3]:


class pairs:
    def __init__(self,numbers,target):
        ans = dict()
        t = 0
        for i in range(0,len(numbers),1):
            for j in range(0,len(numbers),1):
                if (numbers[i] + numbers[j] == target):
                    t = t + 1
                    ans[t] = [i,j]
        print(ans)
        
        
try :
    numbers =[int(i) for i in input('enter the numbers seperated by a comma : ').split(',')]
except:
    numbers = [10,20,10,40,50,60,70]
try:
    target = int(input('enter the target : '))
except:
    target = 50
pairs(numbers,target)


# In[ ]:





# In[ ]:





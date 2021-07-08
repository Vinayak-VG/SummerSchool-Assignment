import numpy as np
n=int(input("enter number : "))
yhat=np.random.rand(n)
y=np.random.randint(0,2,(n))
def O(yhat, y):
   
    return -(y * np.log(yhat) + (1 - y) * np.log(1 - yhat)).mean()
print(yhat)
print(y)
print(O(yhat,y))
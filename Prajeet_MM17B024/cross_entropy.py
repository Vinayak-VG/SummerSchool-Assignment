import numpy as np
import pprint

def cross_entropy(y_hat, y_vec):
	temp = -(1/N) * np.sum(y_vec * np.log2(y_hat) + (1-y_vec) * np.log2(1-y_hat))
	return temp

# print(' ' + 5*'*' + 'Test Cases for Cross Entropy Loss ' + 5*'*')
# y1hat = 

N = int(input(' Input length of data: '))

y_hat = np.random.rand(N)
y_vec = np.random.randint(2, size = N)

O = cross_entropy(y_hat, y_vec)
print(' Cross Entropy loss: {:.5f}'.format(O))
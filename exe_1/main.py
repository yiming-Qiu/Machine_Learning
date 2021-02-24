import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ex1data1.txt', header=None, names=['Population', 'Profit'])
data.head()
#print(data.head())
#print(data.describe())
data.plot(kind='scatter', x='Population', y='Profit', figsize=(12, 8))
#plt.show()

def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner)/(2 * len(X))
data.insert(0,'Ones', 1)

cols = data.shape[1]
X = data.iloc[:, 0:cols-1]
y = data.iloc[:, cols-1:cols]
print(X.head())
print(y.head())
X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0,0]))
print(theta.shape, X.shape, y.shape)

print(computeCost(X, y, theta))

def gradientDescent(X, y, theta, aplha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((aplha / len(X)) * np.sum(term))
        theta = temp
        cost[i] = computeCost(X, y, theta)
    return  theta,cost

alpha = 0.01
iters = 1000

g, cost = gradientDescent(X, y , theta, alpha, iters)
print(g)
print(computeCost(X, y, g))










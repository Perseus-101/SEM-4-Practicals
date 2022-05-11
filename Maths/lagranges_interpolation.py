#Lagranges Interpolation
import numpy as np

x=np.array([0,1,2,4])
y=np.array([1,1,2,5])
val=1.5

def LI(x,y,val):
    sum = 0
    for i in range(len(x)):
        product = 1
        for j in range(len(y)):
            if i!=j:
                product = product*(val-x[j])/(x[i]-x[j])
        sum = sum + product*y[i]
    print('f(x) = ',sum)

LI(x,y,val)

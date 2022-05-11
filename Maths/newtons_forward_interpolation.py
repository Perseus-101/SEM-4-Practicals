#Newton's Forward Interpolation
import numpy as np

x=np.array([10,20,30,40])
y=np.array([9,39,74,116])
val = 15

def NF(x,y,val):
    a=[]
    b=[]
    product = 1
    sum = 0
    
    for i in range (len(x)):
        a.append(y[0])
        y=np.diff(y)    
    print(a)
        
    u = (val-x[0])/(x[1]-x[0])
    
    for j in range (len(x)):
        b.append(product)
        product = product*(u-j)/(j+1)
        
    for i in range (len(x)):
        sum = sum + (a[i]*b[i])
    print('f(x) = ',sum)
    
NF(x,y,val)
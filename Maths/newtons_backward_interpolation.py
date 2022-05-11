#Newton's Backward Interpolation
import numpy as np

x=np.array([1921,1931,1941,1951,1961])
y=np.array([46,66,81,93,101])
val = 1960

def NB(x,y,val):
    a=[]
    b=[]
    product = 1
    sum = 0
    
    for i in range (len(x)):
        a.append(y[-1])
        y=np.diff(y)    
    print(a)
        
    u = (val-x[-1])/(x[1]-x[0])
    
    for j in range (len(x)):
        b.append(product)
        product = product*(u+j)/(j+1)
        
    for i in range (len(x)):
        sum = sum + (a[i]*b[i])
    print('f(x) = ',sum)
    
NB(x,y,val)
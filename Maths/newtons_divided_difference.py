import numpy as np

x=np.array([1,2,4,6,12])
y=np.array([22,30,82,101,216])
val=1.5

def nd(x,y,val):
    a=[]
    b=[]
    sum=0
    product=1

    for i in range(len(x)):
        a.append(y[0])
        y=np.diff(y)
        for j in range(len(y)):
            y[j]=y[j]/(x[i+j+1]-x[j])
    print('Divided differences: ',a)
     
    for i in range(len(x)):
        b.append(product)
        product=product*(val-x[i])
    print(b)
    
    for i in range(len(x)):
        sum=sum+(a[i]*b[i])
    print('f(x) = ',sum)

nd(x,y,val)
         
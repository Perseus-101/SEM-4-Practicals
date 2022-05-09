n = int(input('Enter number of elements: '))
a=[]

for i in range(n):
    elem = int(input('Enter Element: '))
    a.append(elem)

avg=sum(a)/n
print('Average of elements: ', round(avg,2))
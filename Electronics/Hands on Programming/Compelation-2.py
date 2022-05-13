# 4.Number of digits in a number
n = int(input("Enter number: "))
c = 0
while(n>0):
    c = c+1
    n = n//10
print("The number of digits are: ", c)

# 5.Average of inputted numbers
n = int(input('Enter number of elements: '))
a=[]

for i in range(n):
    elem = int(input('Enter Element: '))
    a.append(elem)

avg=sum(a)/n
print('Average of elements: ', round(avg,2))

# 6.Create a function of getting sum of 2 nos
def add(n1,n2):
    return n1+n2

print(add(100,200),'\n',add(8,9))
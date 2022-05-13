# 7.Create Fibonacci Function
# fibonacci main program
import fib_function

fib_function.fib() #Wirte Fibonacci series up to 'n'

# fibonacci function program
def fib():
    i=int(input("Enter 'n': "))
    a = 0
    b = 1
    print(a)
    print(b)
    for j in range(3,i+1):
        next = a + b
        a = b
        b = next
        print(next)

# 8.Bubble Sort
a =[]
num = int(input('Enter number of elements: '))

for i in range(num):
    value = int(input('Enter '+str(i)+' Element: '))
    a.append(value)

for i in range(num-1):
    for j in range(num-i-1):
        if (a[j]> a[j + 1]):
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
print("The sorted list: ", a)
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
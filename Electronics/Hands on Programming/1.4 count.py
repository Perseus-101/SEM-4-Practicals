n = int(input("Enter number: "))
c = 0
while(n>0):
    c = c+1
    n = n//10
print("The number of digits are: ", c)
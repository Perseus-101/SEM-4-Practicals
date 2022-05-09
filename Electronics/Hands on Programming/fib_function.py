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
        
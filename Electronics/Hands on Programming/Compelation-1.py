# 1.Arithmetic Operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nAddition: ", num1 + num2)
print("Subtraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)
print("Division: ", num1 / num2)
print("Floor-division: ", num1 // num2)
print("Exponent: ", num1 ** num2)
print("Modulous: ", num1 % num2)

# 2.Swap two numbers
n1 = int(input("Enter first value: "))
n2 = int(input("Enter second value: "))

print("Numbers before swapping are: ", n1, n2)
temp = n1
n1 = n2
n2 = temp 
print("Numbers after swapping are: ", n1, n2)

# 3.Python Calendar
import calendar
y = int(input("Enter year: "))
m = int (input("Enter month: "))
print(calendar.month(y, m))
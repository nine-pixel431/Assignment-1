print("Hello User!")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
add=num1+num2
sub=num1-num2
mul=num1*num2

if num2 != 0:
    div= num1 / num2
else:
    div= "Undefined (division by zero)"

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)



import sys

def addition(a, b):
    c = a + b
    return c
def subtraction(a, b):
    c = a - b
    return c
def multiplication(a, b):
    c = a * b
    return c
def division(a, b):
    c = a / b
    return c
def wrongChoice():
    print("You made the wrong choice")
    sys.exit()

print("Welcome in easycalc!!!")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = input("""Select the type of activity
1 - addition
2 - subtraction
3 - multiplication
4 - division
I choose: """)

if (c == '1'):
    score = addition(a, b)
elif (c == '2'):
    score = subtraction(a, b)
elif (c == '3'):
    score = multiplication(a, b)
elif (c == '4'):
    score = division(a, b)
else:
    wrongChoice()

print("Result of the action: ", score)

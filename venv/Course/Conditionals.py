is_raining = False
is_cold = False
print("Good Morning")
if is_raining and is_cold:
    print("Bring Umbrella and jacket")
elif is_raining and not is_cold:
    print("Bring Umbrella")
elif not is_raining and is_cold:
    print("Bring Jacket")
else:
    print("Umbrella is optional")

# Exercise
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def temp_conv(z):
    return z*5/9 + 32

print('Select Operation')
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.Temperature Conversion")

while True:
    choice = input("Enter your choice:")
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if choice == '1':
            print(number1, "+", number2, "=", add(num1, num2))
        elif choice == '2':
            print(number1, "-", number2, "=", subtract(num1, num2))
        elif choice == '3':
            print(number1, "*", number2, "=", multiply(num1, num2))
        elif choice == '4':
            print(number1, "/", number2, "=", divide(num1, num2))
        elif choice == '5':
            print(f'{num1} Celsius is equivalent to {temp_conv(num1)} fahrenheit')
        break
    else:
        print("Entered input is invalid")

#  Other code

mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!')
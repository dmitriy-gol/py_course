# Homework 2.1
# It's time to complicate the code -
# let's find the largest of four numbers.

num1 = int(input("number 1: "))
num2 = int(input("number 2: "))
num3 = int(input("number 3: "))
num4 = int(input("number 4: "))

if num1 > num2:
    largest1 = num1
else:
    largest1 = num2

if num3 > num4:
    largest2 = num3
else:
    largest2 = num4

if largest1 > largest2:
    print("Largest number: ", largest1)
else:
    print("Largest number: ", largest2)


# HomeWork 2.4
# Сount mississippily

import time

for i in range(1, 6):
    print(i, 'Mississippi')
    time.sleep(1)
print("Ready or not, here I come!")


# Homework 2.6
# Write the calculator.

operation = input('Select: "+" "-" "*" "/" or "exit":')
while operation == 'exit':
    num1 = int(input("number 1: "))
    num2 = int(input("number 2: "))

    if operation == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operation == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operation == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operation == '/':
        print(f'{num1} / {num2} = {num1 / num2}')

    operation = input('Select: "+" "-" "*" "/" or "exit":')

print("Exit!")

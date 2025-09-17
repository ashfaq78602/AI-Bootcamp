# # Example 1 : Checking a number
# num = 10
# if num > 0:
#     print("Positive Number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative Number")
# print("This is the end of the control flow example.")

# # Example 2: Nested conditions
# age = 25
# if age >= 18:
#     if age < 30:
#         print("You are a young adult.")
#     else:
#         print("You are an adult.")
# else:
#     print("You are a minor.")
# print("This is the end of the nested conditions example.")

# Exercise 1: Check number is prime number
# num = int(input("Enter a number:"))
# is_prime = True
# for i in range(2, int(num**0.5) + 1): # If a number is not divisible by any number up to its square root, it is prime
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime and num > 1:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")
# print("This is the end of the prime number check example.")

# Exercise 2: Create a Menu-Driven Calculator
# def add(a, b):
#     return a + b

# def sub(a, b): 
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     return a / b

# num = int(input("Enter a digit: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division"))
# if num > 0 & num <=4:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))

#     if num == 1:
#         print("The addition is ", add(num1, num2))
#     elif num == 2:
#         print("The subtraction is ", sub(num1, num2))
#     elif num ==3:
#         print("The multiplication is ", mul(num1, num2))
#     elif num == 4:
#         print("The division is ", div(num1, num2))
#     else:
#         print("Wrong Selection")
# else:
#     print("Wrong Selection")

# Exercise 3: Calculate the factorial of a number

# def factorial(num):
#     ans = 1
#     while num > 1:
#         ans *= num
#         num -= 1
#     return ans        
# num = int(input("Enter a number to find its factorial: "))
# print("Result is ", factorial(num))

#Exercise 4: Find the largest number in a list

numbers = []
while True:
    user_input = input("Enter number (Press Q to quit): ")
    if user_input.upper() == "Q":
        print("Quitting..")
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number or Q to quit")

if numbers:
    largest = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > largest:
            largest = numbers[i]
        i += 1
    print("The largest number is ", largest)
else:
    print("No numbers were added.")
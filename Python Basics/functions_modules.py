# def factorial(num):
#     if num == 1 or num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)

# num = int(input("Enter a number to find its factorial: "))
# print("The factorial is ", factorial(num))

#Exercise 2: Importing custom module

# import math_operations

# num1 = 10
# num2 = 5

# print(math_operations.add(num1, num2)) 

#Exercise 3: Check if a number is odd or even

# def oddeven(num):
#     if num % 2 == 0:
#         return "The given number is even"
#     else:
#         return "The given number is odd"
    
# number = int(input("Enter a number to check if odd or even"))
# print(oddeven(number))

#Exercise 4: String Operations
import string_operations as so

phrase = input("Enter a string: ")

print(so.revString(phrase))
print(so.countVowels(phrase))
print(so.checkStrictPalindrome(phrase))
print(so.checkLenientPalindrome(phrase))
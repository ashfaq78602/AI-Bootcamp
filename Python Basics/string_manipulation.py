# # # # # first = 'Hello'
# # # # # second = 'World'
# # # # # result = first + ' ' + second
# # # # # print(result)  # Output: Hello World

# # # # name = "Alice"
# # # # age = 25
# # # # print(f"My name is {name} and I am {age} years old.")

# # # #Split() = uses space unless some other delimiter is given specifically
# # # sentence = "Python is really really fun."
# # # words = sentence.split()
# # # # print(words)

# # # #join() - joins instances of string with given delimiter, usually given space
# # # new_sentence = "|".join(words)
# # # # print(new_sentence)

# # # #replace - to replace a word from sentence
# # # text = "I love JAVA"
# # # updated_text = text.replace("JAVA", "Python")
# # # print(text)
# # # print(updated_text)

# # # #strip() - for cleaned up string at the front and back
# # # stat = "       hello ready for cleaning    "
# # # print(stat)
# # # cleaned_stat = stat.strip()
# # # print(cleaned_stat)

# # #Regular Expression - regex
# # import re
# # text = "Contact me at 123-456-7890"
# # digits = re.findall(r"\d+", text)
# # print(digits)

# # updated_text = re.sub(r"\d", "X", text)
# # print(updated_text)

# #Exercise 1 : Clean the text

# import re

# def clean_text(text):
#     #Remove Punctuation
#     text = re.sub(r"[^\w\s]","",text)
#     #Remove extra spaces
#     text = " ".join(text.split())
#     #Convert to lowercase
#     return text.lower()

# input_text = "    Hello, World.!!! Welcome to Python, Programming....   "
# cleaned_text = clean_text(input_text)
# print(cleaned_text)

#Exercise 2: Check if a string is a Palindrome
# def is_palindrom(text):
#     text = "".join(char.lower() for char in text if char.isalnum())
#     return text == text[::-1]

# input_text = input("Enter a sentence to check for palindrome: ")
# if is_palindrom(input_text):
#     print("The given sentence is a palindrome")
# else:
#     print("The given sentence is not a palindrome")

#Additional Practice
#Program to count number of vowels
# text = "hello worlda"
# count = sum(1 for char in text if char.lower() in "aeiou")
# print(count)

#Program to find and replace all email addresses in a text using regex
# import re
# text = "My email address is ashfaq78602@gmail.com and my wifes email address is way2maryam@gmail.com"
# updated_text = re.sub(r"[a-zA-z0-9._%+-]+@[a-zA-z0-9]+\.[a-zA-z]{2,}","X", text)
# print(updated_text)

#Program to reverse the words in a sentence
text = "Hello My name is Ashfaq Ahmad Khan"
print(text.split()[::-1])

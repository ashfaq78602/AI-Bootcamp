#List - mutable structures

#Creating list
# numbers = [1,2,3,4]
# fruits = ["apple", "banana"]
# mixed = [1, "apple", True]

# #Accessing list
# print(mixed[1])
# print(mixed[-1])
# print(fruits)

# #Adding to List
# fruits.append("orange")
# fruits.insert(1, "grape") #have to give index for insert

# print(fruits)

# # #Removing from List
# # fruits.remove("banana")
# # print(fruits)

# # del fruits[0]
# # print(fruits)

# # fruits.pop() #remove the last item
# # print(fruits)

# #Slicing Lists
# sliced_fruits = fruits[1:3] # from index 1 to before index 3, doesnt takes the item on index 3
# print(sliced_fruits)




#Tuples - immutable structure, cannot be modified but can contain lists that are mutable
# colors = ("red", "green", "blue")
# single_item = ("glass",) #need comma to specify single item tuple

# print(colors[0])
# print(colors[-1])



#Dictionary - key value pair for easy access rather than index, key is used to access item

# student = {"name": "Alice", "age": 2, "grade": "B"}
# print(student)
# print(student["name"])
# print(student["age"])

# student["subject"] = "Math"
# student["age"] = 30
# print(student)

# del student["grade"]
# print(student)

# student.pop("subject") #cannot left empty as lists
# print(student)

# for key, value in student.items(): #for iteration
#     print(key, value)

#Sets - unordered list of unique items, must be of same data type, cannot have duplicate entry

# numbers = {1,2,3,4}
# emptySet = set()
# print(numbers)

# numbers.add(5)
# print(numbers)

# numbers.remove(2)
# print(numbers)

# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1 |set2)
# print(set1 & set2)
# print(set1 - set2)

#Exercise 1 - Manipulate Data in Dictionary

# laptop = {"brand": "apple", "screen": 16, "storage": "1TB"}
# print(laptop)
# laptop["name"] = "macbook pro"
# print(laptop)

# laptop.pop("screen")
# print(laptop)

# if "storage" in laptop:
#     del laptop["storage"]

# print(laptop)

#Exercise 2: Word Frequency Counter
# sentence = input("Enter a sentence:")

# #Split sentence into words
# words = sentence.split()

# word_count = {}

# for word in words:
#     word = word.lower()
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print(word_count)

#Exercise 3: reverse a list and remove duplicates using a set
list = [1, 2, 3, 4, 5, 1, 2, 3]
reversed_list = list[::-1]
unique_set = set(reversed_list)

print("Reversed List:", reversed_list)
print("Unique Set:", unique_set)

#Exercise 4: store student grades in a dictionary and calculates the average grade
reynis = {"English": 7, "Math": 9, "Science": 9, "Computer": 10}
total = 0
for grade in reynis.values():
    total += grade
average = total/len(reynis.values())

print("Average: ",average)

average = sum(grade for grade in reynis.values()) / len(reynis.values())
print(average)


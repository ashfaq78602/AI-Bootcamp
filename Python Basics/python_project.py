#[expression for items in iterable if condition]

#Create a list of squares
# squares = [x**2 for x in range(10)]
# print(squares)

#Filter even numbers
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)

#Lambda Functions - single expression functions
# add = lambda x, y: x + y
# print(add(3,5))

#map() - applies a function to each item in an iterable
numbers = [1,2,3,4]
squares = map(lambda x: x**2, numbers)
print(list(squares))

#filter() - filters item based on a condiion
evenList = filter(lambda x: x % 2 == 0, numbers)
print(list(evenList))

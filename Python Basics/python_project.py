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

#map()
numbers = [1,2,3,4]
squares = map(lambda x: x**2, numbers)
print(list(squares))
"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, 
but can only have one expression.


Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
"""

# x = lambda a : a + 10
# print(x(5))




# x = lambda a, b : a * b
# print(x(5, 6))




# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))





# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# print(mydoubler(11))
# mytripler = myfunc(3)
# print(mytripler(11))
# mydoubler = myfunc(2)
# print(mydoubler(11))
# mytripler = myfunc(3)
# print(mytripler(11))


# """
# Lambda with Built-in Functions
# Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().

# Using Lambda with map()
# The map() function applies a function to every item in an iterable:
# """
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#The filter() function creates a list of items for which a function returns True:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#The sorted() function can use a lambda as a key for custom sorting:
students = [("Emil", 25,["class",12]), ("Tobias", 22,["class",2]), ("Linus", 28,["class",8])]
sorted_students = sorted(students, key=lambda x: x[2][1])
print(sorted_students)




words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
print(sorted_words)


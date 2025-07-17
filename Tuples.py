# Tuple

# mytuple=("apple","book","stop")
# print(mytuple)
#
# print(type(mytuple))

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
#
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#
# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# this_tuple = (1, 2, 3)
# this_is_not_tuple = ("A")
# print(type(this_tuple))
# print(type(this_is_not_tuple))

# Tuple Items - Data Types
# Tuple items can be of any data type:

# tuple1 = (1, 2, 3)
# tuple2=("a", "b", "c")
# tuple3=(True, False, True)
# print(tuple1)
# print(tuple2)
# print(tuple3)
# tuple1 = ("abc", 34, True, 40, "male")
# print(tuple1)

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:

# tuple1 = (1, 2, 3)
# print(tuple1[1])

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
#
# When specifying a range, the return value will be a new tuple with the specified items.


# thistuple = ("apple", "banana", "cherry","book","dfdsg","gdayfs")
# print(thistuple[2:5])

# Check if Item Exists

# thislist = ["apple", "banana", "cherry"]
# if 'apple' in thislist:
#     print("Yes, apple is in the list")

# Python - Update Tuples

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# tuple1 = (1, 2, 3)
# x=list(tuple1)
# print(x)
# x[1]=213
# print(x)
# tuple1=tuple(x)
# print(tuple1)

#append
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# thistuple = ("apple", "banana", "cherry")
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = ("apple", "banana", "cherry")
# thistuple+=tuple1
# print(thistuple)

#remove
# thistuple = ("apple", "banana", "cherry")
# y=list(thistuple)
# y.remove("banana")
# thistuple=tuple(y)
# print(thistuple)


# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)

# Python - Unpack Tuples
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# Packing a tuple:
#
# fruits = ("apple", "banana", "cherry")

# Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# fruits=("apple","banana","orange","strawberry")
# (a,b,c,d)=fruits
# print(a)

# Using Asterisk*

# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# fruits=("apple","banana","orange","strawberry")
# (a,b,*c)=fruits
# print(a)
# print(b)
# print(c)


# Python - Loop Tuples

# fruits=("apple","banana","orange","strawberry")
# for fruit in fruits:
#     print(fruit)

# Join Two Tuples
# fruits1=("apple","banana")
# fruits2=("apple","banana")
# fruits_join=fruits1+fruits2
# print(fruits_join)

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2
# print(mytuple)

#count method
# thistuple=(1,3,2,42,24,1,32)
# print(thistuple.count(1))

# Python Tuple index() Method
# thistuple=(1,3,2,123,4,23,23,23,23,321)
# print(thistuple.index(23))


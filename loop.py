# Python If ... Else

# Python Conditions and If statements
# a=23
# b=3
# if a>b:
#     print(a ,"A is greater than B")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

# a = 33
# b = 200
#
# if b > a:
#   pass

# Python Match
# The match statement is used to perform different actions based on different conditions.


# day=5
# match day:
#     case 1:
#         print(day,"not match")
#     case 2:
#         print(day,"not match")
#     case 3:
#         print(day,"not match")
#     case 4:
#         print(day," match")
#     case 5:
#         print(day," match")
#     case 6:
#         print(day,"not match")

# day = 4
# match day:
#   case 6:
#     print("Today is Saturday")
#   case 34:
#     print("Today is Sunday")
#   case _:
#     print("Looking forward to the Weekend")

# while Loop

# i=4
# while i>0:
#     print(i)
#     i-=1


# Python For Loops

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:

# item=["apple","banana","orange"]
# for i in item:
#     if i=="apple":
#         continue
#     print(i)


# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.


# lsit=[1,2,3,4,5]
# for i in range (len(lsit)):
#     print(lsit[i])
#
# for x in range(6):
#   print(x)


# for x in range(2,42,2):
#     print(x)

# Else in For Loop


# for x in range(2,42,2):
#     print(x)
# else: print("Finish!")

# Nested Loops
# A nested loop is a loop inside a loop.
#
# The "inner loop" will be executed one time for each iteration of the "outer loop":

# list=["a","b","c"]
# list2=["apple","banana"]
#
# for i in list:
#     for j in list2:
#         print(i,j)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

# for x in [1,32,2]:
#     pass
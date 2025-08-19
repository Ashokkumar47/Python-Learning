# Python Functions
# A function is a block of code which only runs when it is called.



# def my_function():
#     print("Hello World")
#
# my_function()


# Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comm


# def value_show(val):
#     print(val)
#
# value_show(5)
# value_show("hello world")

# def my_function(fname, lname,one):
#   print(fname + " " + lname)
#
# my_function("Emil", "Refsnes",1)


# Arbitrary Arguments, *args

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

# def my_function(*params):
#     print(params)
# my_function(1, 2, 3)

# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.

# def my_function(one, two):
#     print(one)
#     print(two)
#
#
#
# my_function(two=1,one= 2)

# Arbitrary Keyword Arguments, **kwargs

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.


# This way the function will receive a dictionary of arguments, and can access the items accordingly:

#
# def my_function(**kid):
#   print("His last name is " + kid["lname"])
#
# my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
# def my_function(company_name="ABC"):
#     print("Hello " + company_name)

# my_function("abc")


# Passing a List as an Argument

# def fun(fruit):
#     # print('Hello World', fruit)
#      for x in fruit:
#          print(x)
#
# fruits = ['apple', 'banana', 'orange']
# fun(fruits)

# Return Values
# To let a function return a value, use the return statement:

# def sum_fun(value):
#     return 5+value
# print(sum_fun(1112))

# The pass Statement

# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
# def fun():
#     pass

# Positional-Only Arguments
# Recursion
# Python also accepts function recursion, which means a defined function can call itself.

# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("Recursion Example Results:")
# tri_recursion(6)

# Python Lambda
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression

# Syntax
# lambda arguments : expression

# add

# x=lambda a : a+10
# print(x(5))


# Lambda functions can take any number of arguments:
#
# x=lambda a,b:a+b
# print(x(2,4))

# Why Use Lambda Functions?

# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
# def myfunc(n):
#   return lambda a : a * n
#
# print(myfunc(3))
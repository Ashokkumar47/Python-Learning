# print("hello world")
# Syntax is about the correct arrangement of words and symbol in a code like correct structer
## semantics refer to the meaning or the interpretation of a symbol , characters and commend in a language It is about whast the code is supposed to do when it runs

'''Syntax and Semantics in Python
Single line Comments and multiline comments
Definition of Syntax and Semantics
Basic Syntax Rules in Python
Understanding Semantics in Python
Common Syntax Errors and How to Avoid Them
Practical Code Examples
Syntax refers to the set of rules that defines the combinations of symbols that are considered to be correctly structured programs in a language. In simpler terms, syntax is about the correct arrangement of words and symbols in a code.

Semantics refers to the meaning or the interpretation of the symbols, characters, and commands in a language. It is about what the code is supposed to do when it runs.'''
from time import process_time_ns

##python is case sensitive

# print("Hello World")
#
# name="ashok"
# Name="RAj"
# print(Name)
# print(name)

##indentation
''' Indentation in Python is used to define the structer and hierarchy of a code , python uses indendation to determine the grouping of statements. '''


# age=110
# if age>18:
#     print("Age is greater than 18")
# else:
#     print("Age is less than 18")

#line Continuation


# total=1+2+43+543+345+3+2+34+\
#      +435
# print(total)


# multipe sagment in one line
# x=45;y=24;z=23;a=x+y+z
# print(x)


# age=24
# name="ashok"
# print(type(age))
# print(type(name))



#segmentation error
# age= 34
# if age > 18:
#     print("hello")

# a=b


# if True:
#     print("First line")
#     if False:
#         print("Second line")
#     print("Third line")
# print("Fourth line")


##Variables
# a=20
#a is variable  and 20 is value
#
# age=34
# height=6.2
# name="Krish"
# is_student=True
#
# print(age)
# print(height)
# print(name)
# print(is_student)

##naming convention
#variable name should be descriotive
# variable name should be case senstive

# first_name="Ashok"
# last_name="kumar"


#invalid variable
# 2age=34
# first-name="Ashok"
# @name="krish"


##understanding the variable type
##python is dynamically typed and a variable is determined at runtime

# age=24
# height=6.3
# name="ashok"
# is_student=True
# print(type(age))

##type checking and conversion

# variable name should be case sensitive
# first_name="ashok"
# Last_name="Kumar"
# print(first_name,Last_name)

#invalid Name
# 2age=45
# print(2age)
# @name="ashok"

# Case senstive
# Name="ashok"
# name="kumar"

##Type checking and conversion
# age=35
# name='John'
# height=6.9
# is_student=True

#type Checking
# print(type(age))
# print(type(name))
# print(type(height))
# print(type(is_student))

#type conversion
# print(type(str((age))))
# print(type(str(name)))
# print(type(str(height)))
# print(type(str(is_student)))

# print(type(name))
# print((bool((height))))

# print(type(int((name))))
# print(float(int((height))))

#Dynamic typing
#python Allow the type of variable to change as the program execute

# var=10
# print(var,type(var))
# var=7.5
# print(var,type(var))
# var="Ashok"
# print(var,type(var))

#Type of variable
# text-- str
# numberic -- int float  complex
# sequesnce -- list , tuple , range
#mapping -- Dict
#set-- set, frozenset
#boolen Type --bool
# binary Type-bytes, bytearray, memoryview
#none Type --- NoneType



# num=5j
# # print(type(num))
# name=['John','Joe',23]
# print(type(name))


# text- str
# number- int float, complex
# sequence -- list , tuple ,range
# none type =NoneType
# set- set , frozenset
# mapping -dict
# boolean type - bool
# Binary Type - bytearray , memoryview ,bytes


# x,y,z=age,name,height;
# print(x,y,z)

# x=y=z=age
# print(x,y,z)

# fruit=['apple','banana','orange']
# x,y,z=fruit
# print(x+y+z)

#Global Variable
# companyName="Ashok prime"
#
# def my_function():
#     print("My company name is" , companyName)
#
# my_function()

#same name on local variable
# companyName="Ashok prime"
#
# def my_function():
#      companyName="Ashok patel"
#      print("My company name is" , companyName)
#
# my_function()
# print(companyName)


#global variable inside the function
# def my_function():
#     global companyName;
#     companyName='John'
#     print(companyName)
#
# my_function()
# print(companyName)

#use the global keyword if you want to change a global variable inside a function.

# companyName="ashok prime"
#
# def my_function():
#     global companyName;
#     companyName="ashok patel"
#     print(companyName)
#
# my_function()
# print(companyName)

# x='ashok'
# age=35
# height=6.9
# comp=3+4j
# print(type(comp))

# company_name=["apple","google","lava","jeee"] #list
# first_company=company_name[0]
# print(first_company)

# company_name=('apple','google',"lava")   #tuple
# print(company_name)

# x=range(6)     #range
# print(x)
# print(type(x))
# print(len(x))

# Dict
# x={"name":"ashok","height":6.2}
# y=x["name"]
# print(x)
# print(y)


#set
# x=set(('apple','book'))
# print(type(x))

#frozenset
# x=frozenset({age,name,height,is_student})
# print(type(x))

#boolean
# x=bool(6)
# print(x)
# print(type(x))

#bytes
# x=bytes(8)
# print(x)
# print(type(x))

#bytearray
# x=bytearray(5)
# print(x)

#memoryview
# x=memoryview(bytes(5))
# print(x)

# x = 1    # int
# y = 2.8  # float
# z = 1j #complex
# print(x,y,z)
# print(type(x),type(y),type(z))

# x = 1
# y = 35656222554887711
# z = -3255522
#
# print(type(x))
# print(type(y))
# print(type(z))
# print(x,y,z)

# Type Conversion
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex
# a=complex(x)
# Note: You cannot convert complex numbers into another number type.
# print(type(b))
#
# print(b)


# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
# import random
# x=random.randrange(1,10)
# print(x)

# Python Casting

# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3") # z will be 3
# print(x,y,z)

#Multiline Strings
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# a = "Hello, World!"
# print(len(a))

# for x in "apple":
#     print(x)
# for x in range(10):
#     print(x)


# x="I am free"
# if "free" not in x:
#     print("yes I am free ")
# else:
#     print("I am not free")

# Python - Slicing Strings
# b = "Hello, World!"
# print(b[2:5])


# a = "Hello, World!"

# a= "ashok kumar is Good"
# x=a.upper()
# y=a.lower()
# print(x)
# print(y)

# Remove Whitespace
# a="ashok kumar    "
# print(a.strip())

#Replace String
# a="ashok kumar"
# print(a.replace("a","b"))
# print(a)

#Split String
# a = "Hello, World!"
# b=a.split(",")
# print(b)

# F-Strings
# age=18
# txt=f"age is {age:.2f}"
# print(txt)

# Escape Character
# txt = "We are the so-called "Vikings" from the north."
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)
# x="hello ashok how are you"
# print(x.capitalize())

#String center() Method
# x="ashok"
# print(x.center(20,"@"))

#boolean
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 33
# if a > b:
#     print('a is greater than b')
# else:
#     print('a is less than b')


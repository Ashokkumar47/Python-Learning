# Python OOP
# OOP stands for Object-Oriented Programming.

# Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.
# Advantages of OOP
# Provides a clear structure to programs
# Makes code easier to maintain, reuse, and debug
# Helps keep your code DRY (Don't Repeat Yourself)
# Allows you to build reusable applications with less code

# Tip: The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.4

# What are Classes and Objects?
# Classes and objects are the two core concepts in object-oriented programming.
# A class defines what an object should look like, and an object is created based on that class. For example:

# Class	Objects
# Fruit	Apple, Banana, Mango
# Car	Volvo, Audi, Toyota

# When you create an object from a class, it inherits all the variables and functions defined inside that class.





# Python Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.


# Create a Class

class my_class:
    x=5


# print(type(my_class))
# print(my_class.x)

# create object
# Now we can use the class named MyClass to create objects:


# Create an object named p1, and print the value of x:

# p1=my_class()
# print(p1.x)

# The __init__() Function


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# p1=person("ashok",22)
# print(p1.name)
# print(p1.age)

# class my_class:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#
# C1=my_class(10,20)
# print(C1.x,C1.y)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f'{self.name} and {self.age} years old'
#
# p1=Person('John',20)
# print(p1)

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.


# class person_new:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greeting(self):
#         print("Hello " + self.name +"! best Wish for Your Birthday!")
#
# p1=person_new("John",20)
# p1.greeting()

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# The self Parameter

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:


# class person_data:
#     def __init__(one,name,age):
#         one.name=name
#         one.age=age
#     def greeting(one):
#         print("Hello",one.name ,"your age is ",one.age)
#
# p1=person_data("John",20)
# p1.greeting()
# p1.age=22
# p1.greeting()

# Modify Object Properties
# class person_data:
#     def __init__(one,name,age):
#         one.name=name
#         one.age=age
#     def greeting(one):
#         print("Hello",one.name ,"your age is ",one.age)
#
# p1=person_data("John",20)
# p1.greeting()
# p1.age=22
# p1.greeting()

# Delete Object Properties
# class person_data:
#     def __init__(one,name,age):
#         one.name=name
#         one.age=age
#     def greeting(one):
#         print("Hello",one.name ,"your age is ",one.age)
#
# p1=person_data("John",20)
# p1.greeting()
# p1.age=22
# p1.greeting()
# del p1.age
# p1.age=25
# p1.greeting()


# Delete Objects

# class person_data:
#     def __init__(one,name,age):
#         one.name=name
#         one.age=age
#     def greeting(one):
#         print("Hello",one.name ,"your age is ",one.age)
#
# p1=person_data("John",20)
# p1.greeting()
# p1.age=22
# del p1
#
# p1.greeting()
# del p1.age
# p1.age=25
# p1.greeting()

# The pass Statement
# class Person:
#   pass

# Python Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.
# Create a Parent Class

class Person:
    def __init__(self,FirstName,LastName):
        self.FirstName=FirstName
        self.LastName=LastName
    def printname(self):
        print(self.FirstName,self.LastName)

p1=Person("John","Smith")
p1.printname()

# child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

# class dummy(Person):
#     pass
#
# p2=dummy("Raj","Kumar")
# p2.printname()


# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.

# class Person:
#     def __init__(self,FirstName,LastName):
#         self.FirstName=FirstName
#         self.LastName=LastName
#     def printname(self):
#         print(self.FirstName,self.LastName)
#
# class student(Person):
#     def __init__(self,FirstName,LastName):
#         Person.__init__(self,FirstName,LastName)
#
# x=student("John1","Smith")
# x.printname()

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:


# class Person:
#     def __init__(self,rollNumber,name):
#         self.rollNumber=rollNumber
#         self.name=name
#
#     def printname(self):
#         print(self.rollNumber,self.name)
#
# class Student(Person):
#     def __init__(self,rolNumber,name):
#         super().__init__(rolNumber,name)
#
# x=Student(34,"Ashok")
# x.printname()

# Add Properties

class Person:
    def __init__(self,FirstName,LastName):
        self.FirstName=FirstName
        self.LastName=LastName

    def printname(self):
        print(self.FirstName,self.LastName)

class Student(Person):
    def __init__(self,FirstName,LastName):
        Person.__init__(self,FirstName,LastName)
        self.Year=2342


# x=Student("John","Smith")
# x.printname()
# print(x.Year)

# class Student2(Person):
#     def __init__(self,FirstName,LastName,Year):
#         Person.__init__(self,FirstName,LastName)
#         self.Year=Year
#
# x=Student2("John","Smith",426)
# print(x.Year)

# Add Methods

class lab:
    def __init__(self,bookName,bookYear,Author):
        self.bookName=bookName
        self.bookYear=bookYear
        self.Author=Author

    def printname(self):
        print(self.bookName,self.bookYear,self.Author)

class college(lab):
    def __init__(self,bookName,bookYear,author):
        lab.__init__(self,bookName,bookYear,author)

    def print_college(self):
        print(self.bookName,self.bookYear,self.Author)

x=college("the love one",2002,"Raj Kumar")
x.print_college()

# Python Iterators
# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:


student=("Ashok","age=35","jai ho")
itt=iter(student)
print(next(itt))
print(next(itt))
print(next(itt))

s1="ashok"
si=iter(s1)
print(next(si))
print(next(si))
print(next(si))
print(next(si))
print(next(si))

# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.


# class number:
#     def __iter__(self):
#         self.a=1
#         return self
#
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
#
# mynuber=number()
# n1=iter(mynuber)
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))
# print(next(n1))

# StopIteration

# class number:
#     def __iter__(self):
#         self.a=1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#           raise StopIteration
#
# mynuber=number()
# n1=iter(mynuber)


# Python Polymorphism
# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.
# Function Polymorphism
# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():


class bmw:
    def __init__(self,year,time):
        self.year=year
        self.time=time
    def printDetails(self):
        print(self.year,self.time)

class bmw2:
    def __init__(self,year,time):
        self.year=year
        self.time=time
    def printDetails(self):
        print(self.year,self.time)

class bmw3:
    def __init__(self,year,time):
        self.year=year
        self.time=time
    def printDetails(self):
        print(self.year,self.time)

car1=bmw("1999","10")
car2=bmw2("19934","10")
car3=bmw3("199324","10")

for x in [car1,car2,car3]:
    x.printDetails()

# Inheritance Class Polymorphism

class company:
    def __init__(self,Name,est):
        self.Name=Name
        self.est=est
    def printdetails_of_company(self):
        print(self.Name,self.est)

class new_company(company):
    def printdetails_of_company(self):
        print(self.Name,self.est)
class old_company(company):
    def printdetails_of_company(self):
        print(self.Name,self.est)

c1=new_company("Vasitum","2017")
c2=old_company("Maven","2000")
c1.printdetails_of_company()
c2.printdetails_of_company()


# Python Scope
# A variable is only available from inside the region it is created. This is called scope.
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# def fun():
#     x=300
#     def fun2():
#         print(x)
#     fun2()
#
# fun()

# Global Scope
# Python Modules

# Create a Module

# To create a module just save the code you want in a file with the file extension .py:

# import greeting
# greeting.Greeting("ashok")

# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:

# Python Dates
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
# import datetime
# x=datetime.datetime.now()
# print(x)
# Creating Date Objects
# import datetime
# x=datetime.datetime(2020,8,21)
# print(x)

# Project


# n=input("enter your name")
# result=[]
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         result.append("FizzBuzz")
#     elif i%3==0:
#         result.append("Fizz")

# nums=[2,1,34,23,32,2]
# num1=[]
# val=2
# count=0
# #loop
# for i in range(len(nums)):
#     if nums[i]!=val:
#         num1.append(nums[i])
#     else:
#         count+=1
#         pass
# print(num1)
# print(count)
# print(len(num1))
# for i in count:
#     num1.append("_")
# print(num1)




# Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# thisdict={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"a":56}
# print(thisdict)
# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict.items())
# print(thisdict.get("a"))
# print(thisdict.get("c"))
# print(len(thisdict))
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# dict() Constructor
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# dict={'a':1,'b':2,'c':3}
# dict['d']=4
# print(dict)
# dict1={'a':5,'b':2002,'c':2}
# print(dict1['a'])
# x=dict1['a']
# print(x)

# get
# y=dict1.get('a')
# print(y)
# y=dict1.keys()
# print(y)
# y=dict1.values()
# print(y)



dict_a={
    "name":"ashok",
    "age":22,
    "city":"UK",
    "country":"UK",
    "province":"UK",
}
#
# x=dict_a.values()
# y=dict_a.keys()
# dict_a["mobile"]=5634434
# print(dict_a)


# print(dict_a.get("name"))
# print(dict_a.items())

# Change Dictionary Items

# dict_a["name"]="ashok Kumar"
# print(dict_a)

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
#
# The argument must be a dictionary, or an iterable object with key:value pairs.

# Add Dictionary Items
# dict_a["Last Name"]="AK47"
# print(dict_a)

dict_a.update({"last Name":"AK47"})
print(dict_a)
# dict_a.popitem()
# print(dict_a)

# for k in dict_a:
#     print(k)

# for v in dict_a:
#     print(dict_a[v])

# You can also use the values() method to return values of a dictionary:
# for i in dict_a.values():
#     print(i)

# You can use the keys() method to return the keys of a dictionary:

# for i in dict_a.keys():
#     print(i)
#
# for i in dict_a.items():
#     print(i)

# Copy a Dictionary

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# new_dict_a = dict_a.copy()
# print(new_dict_a)

# Another way to make a copy is to use the built-in function dict()
# Nested Dictionaries

school_student={
    "student1":{
        "name":"One",
        "age":22,
        "city":"UK",
    },
    "student2":{
        "name":"Two",
        "age":23,
        "city":"USA",
    }
}
print(school_student)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])






# Python Sets
# myset = {"apple", "banana", "cherry"}
# print(myset)
# print(type(myset))

# Unordered
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# thisset={"a","b","c","d","e","f","g","h","a"}
# print(thisset)
# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

# Length of a Set
# oneset={"a","b","c","d","e","f","g","h","a","b","c","d","e","f","g","h"}
# print(len(oneset))

# The set() Constructor
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)


# thisset={'a','b','c','d','e','f','g','h'}
# for item in thisset:
#     print(item)

# Add Items
# Once a set is created, you cannot change its items, but you can add new items.

# thisset={'a','b','c','d','e','f','g','h'}
# thisset.add('h')
# print(thisset)

# Add Sets
# To add items from another set into the current set, use the update() method.

# thisset={'a','b','c','d','e','f','g','h'}
# thisset1={1,2,3,4,5}
# thisset.update(thisset1)
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
#
# thisset.update(mylist)
#
# print(thisset)

#remove
# thisset={'a','b','c','d','e','f','g','h'}
# thisset.remove('a')
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
#
# x = thisset.pop()
#
# print(x)
#
# print(thisset)


# loop
# thisset={"a","b","c","d","e","f","g","h"}
# for item in thisset:
#     print(item)

# Python - Join Sets
# set1={1,2,3,4,5}
# set2={1,2,3,4,5}
# set3=set1.union(set2)
# print(set3)

# Method	Shortcut	Description
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not
#  	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
#  	>	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others



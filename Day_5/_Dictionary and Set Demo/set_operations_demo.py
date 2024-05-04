"""
Theory: 

Sets are unordered and unique and immutable elements Operations possible :
1)    ADD : add(X) [single element] / update({a,b,c}) [Multiple elements]
2) Delete :remove(X) / discard(X) / difference_update({a,b,c}) [Multiple elements]
3) select / Update -- no such operation required since there is no subscripts   
4) all other set sepcific operations like difference etc 
"""

my_set = { 1,2,3,43,4,5,5,6,7,7,7,8,8,8,8,"gaurav","Pune",
            ("dbda,hpcsa","diot","dac"),frozenset({"dbda,hpcsa","diot","dac"})
          }

# print( len(my_set))
my_subset1 = {100,200,300}
my_subset2 = {1,2,3,300}

print("------------------------")
print(my_set) 

print("------------------------")
print(my_subset1)

print("-----------------------")
print(my_subset2)
# print(my_set[0]) # TypeError: 'set' object is not subscriptable

print("Operations on sets ")
print("===========================================")

# print(" ----------------------- TESTS Operations ----------------------------------")

# print("len(s) -- Return the number of elements in set s (cardinality of s)")
# print(len(my_subset1))

# print("x in s --Test x for membership in s.")
# print(100 in my_subset1)

# print(frozenset({"dbda,hpcsa","diot","dac"}) in my_set)
# print(("dbda,hpcsa","diot","dac") in my_set)
# print("dbda" in my_set)
# print("Pune" in my_set)


# print("x not in s --Test x for non-membership in s.")
# print(100 not in my_subset1)

# print("isdisjoint(other) --Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.")
# print(my_set.isdisjoint(my_subset1))
# print(my_set.isdisjoint(my_subset2))


# print("""
# issubset(other)
# set <= other
# Test whether every element in the set is in other.
# set < other
# Test whether the set is a proper subset of other, that is, set <= other and set != other.
#       """)

# print(my_subset1)
# print(my_subset2)
# print(my_set)
# print(my_subset1.issubset(my_set))
# print(my_subset2.issubset(my_set))




# print(""" 
#       issuperset(other)
#       Test whether every element in other is inthe set.
#       set >= other

#       set > other
#       Test whether the set is a proper supersetof other, that is, set >= other and set !=other.
#       """)

# print(my_set.issuperset(my_subset1))
# print(my_set.issuperset(my_subset2))



# print(" ----------------------- Normal SET Operations ----------------------------------")
# print("""
#       union(*others)
#       set | other | ...
#       Return a new set with elements from the set and all others.
#       """)

# print(my_subset1)
# print(my_subset2)
# print("return_val: ", my_subset1.union(my_subset2))
# print('actual set ' , my_subset1)







# print("""
#       intersection(*others)
#         set & other & ...
#         Return a new set with elements common to the set and all others.
#       """)

# print(my_subset1)
# print(my_subset2)
# print(my_subset1.intersection(my_subset2))
# print(my_subset1)






# print(""" 
#       difference(*others)
#         set - other - ...
#         Return a new set with elements in the set that are not in the others.
#       """)
# print(my_subset1)
# print(my_subset2)
# print(my_subset1.difference(my_subset2))
# print(my_subset2.difference(my_subset1))
# print(my_subset1)






# print("""
#       symmetric_difference(other)
#         set ^ other
#         Return a new set with elements in either the set or other but not both.
#       """)
# print(my_subset1)
# print(my_subset2)
# print(my_subset1.symmetric_difference(my_subset2))
# print(my_subset1)





# print("""
#       copy()
#         Return a shallow copy of the set.
#       """)

# my_copy_set = set()
# print(my_copy_set)
# my_copy_set = my_subset1.copy()
# print(my_copy_set)





# print(" ----------------------- Update Operations ----------------------------------")
# print("Note, the non-operator versions of the update(), intersection_update(), difference_update(), and symmetric_difference_update() methods will accept any iterable as an argument.")
# print("""
#       update(*others)
#         set |= other | ...
#         Update the set, adding elements from all others.
#       """)
# print(my_subset1)
# print(my_subset2)
# # trying to add multiple values which happens to come from list here 
# my_subset1.update(my_subset2)
# print(my_subset1)

# trying to add multiple values which happens to come from set here 
# my_subset1.update({789654,4574985,340928409})
# print(my_subset1)






# print("""
#       intersection_update(*others)
#         set &= other & ...
#         Update the set, keeping only elements found in it and all others.
#       """)

# print(my_subset1)
# print(my_subset2)
# # trying to add multiple values which happens to come from list here 
# my_subset1.intersection_update(my_subset2)
# print(my_subset1)






# print("""
#         difference_update(*others)
#         set -= other | ...
#         Update the set, removing elements found in others.      
#       """)

# print(my_subset1)
# print(my_subset2)

# # trying to add multiple values which happens to come from list here 
# my_subset1.difference_update(my_subset2)
# print(my_subset1)





# print(""" 
#     symmetric_difference_update(other)
#     set ^= other
#     Update the set, keeping only elements found in either set, but not in both.
# """)

# print(my_subset1)
# print(my_subset2)
# # trying to add multiple values which happens to come from list here 
# my_subset1.symmetric_difference_update(my_subset2)
# print(my_subset1)




# print(" ----------------------- Mutable Operations ----------------------------------")

# print("""add(elem)
#         Add element elem to the set.""")

# my_copy_set = set()
# print(my_copy_set)

# #add only one value
# my_copy_set.add(7)
# # my_copy_set.add({789654,4574985,340928409}) # TypeError: unhashable type: 'set'
# #add multiple values
# my_copy_set.update({7,45,34})
# print(my_copy_set)





print("""
    remove(elem)
        Remove element elem from the set. Raises KeyError if elem is not contained in the set.
      """)
# print(my_copy_set)
# my_copy_set.remove(789654)
# my_copy_set.difference_update({789654,4574985,340928409})
# print(my_copy_set)
# my_copy_set.remove(789654) #KeyError: 789654




# print("""
#     discard(elem)
#         Remove element elem from the set if it is present.
#       """)
# print(my_copy_set)
# my_copy_set.discard(789654)
# print(my_copy_set)
# my_copy_set.discard(789654)
# print(my_copy_set)





# print("""
#     pop()
#         Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.
#       """)
# my_copy_set.add(789654)
# my_copy_set.add(11111)
# my_copy_set.add(2222)
# print(my_copy_set)
# my_copy_set.pop()
# print(my_copy_set)

# print("""
#     clear()
#     Remove all elements from the set.
#       """)
# print(my_copy_set)
# my_copy_set.clear()
# print(my_copy_set)


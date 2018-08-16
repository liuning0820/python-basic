# refer to same object and has same value
a = 1
b = 1
print(a == b)
print(a is b)

b =2 
print(a)

a = 'cat'
b = 'cat'
print(a == b)
print(a is b)
    

#  The two lists are equivalent, because they have the same elements,
#  but not identical,because they are not the same object.
a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)

b[0]=17
print(a)

# The association of a variable with an object is called a reference
# An object with more than one reference, so we say that the object is aliased
a = [1,2,3]
b = a
print(a == b)
print(a is b)

b[0]= 17
print(a)


# -*- coding: utf8 -*-

# list是一个可变的有序表
classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))

# The 'in' operator works in list
print(bool('Bobs' in classmates))

print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# Traversing a list
for classmate in classmates:
    print(classmate)

for i in range(len(classmates)):
    print('classmates[', i, '] = ', classmates[i])

classmates.pop()
print('classmates =', classmates)

# TypeError: 'str' object does not support item assignment
# classmate[-1] = 'Toby'
# print('classmates =', classmates)


# list operation

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
d = c * 3
print(c)
print(d)

# update Type 'int' object in list
a[-1] = 'test'
print(a)

# list slices

slice_sample = [12, 32, 34, 54, 89]
print(slice_sample[1:3])
print(slice_sample[:3])
slice_sample[1:]

# list methods

method_sample_1 = [6, 2, 3]
method_sample_1.append(4)
print(method_sample_1)

method_sample_2 = [4, 5]
method_sample_1.extend(method_sample_2)
print(method_sample_1)
method_sample_1.sort()
print(method_sample_1)

# delete element

delete_sample = ['a', 'b', 'c']

deleted_item = delete_sample.pop(1)
print(delete_sample)
print(deleted_item)

del delete_sample[1]
print(delete_sample)

delete_sample.remove('a')

print(delete_sample)



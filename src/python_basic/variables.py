#!/usr/bin/python
#coding:UTF-8
__author__ = 'toby'

x = 1
print(x)

x = "foo"

print(x)

x=x+"1"

print(x)

pi = 3.1415926535897931
print(type(pi))
print(pi)




y = input('hi,tell me something\n')

print(y)



#变量交换
a = 123
b = 456
a,b = b,a

print(a)
print(b)


#带有索引位置的集合遍历
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print (i, '--->', colors[i])

for i, color in enumerate(colors):
    print (i, '--->', color)



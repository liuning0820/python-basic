# coding:UTF-8
import sys


# 添加自定义的模块库
# print(sys.path.append('/home/pi/py/modules'))



# 名称空间与作用域：内建名称空间，全局名称空间，局部名称空间
# ./images/名称空间-变量作用域.JPG
# 名称空间考虑的是“他存在吗”的问题
# 变量作用域考虑的是“我能看见他吗”的问题 （存在覆盖问题）
print(globals())
a = 5
print(locals())  # 内建，全局的也能作用于local的scope内

# 导入模块 import modulename

# 导入指定模块属性 from moduleX import nameX

# 给导入模块赋别名 import moduleX as mY

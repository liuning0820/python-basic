# coding:UTF-8
import math

# The function random returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0)
import random

for i in range(10):
    x = random.random()
    print(x)

# The function randint takes the parameters low and high,
# and returns an integer between low and high (including both).
print(random.randint(5, 10))

t = [1, 2, 4, 6]
print(random.choice(t))


def square_sum(a, b):
    return a ** 2 + b ** 2


# user defined function.this is also a void function( with no return value)

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()


# function with return value.
def add_number(a, b):
    'add a with b and return the sum.'
    added = a + b
    return added


# test the function and print the result
x = add_number(3, 5)
print(x)

# Function Attributes 函数属性
# https://www.python.org/dev/peps/pep-0232/
add_number.version = 0.1
print(add_number.version)
print(add_number.__doc__)
print(add_number.__dict__)


# functions.py
# Defining Functions

# def starts a function definition
# names of functions follow variable naming conventions
# functions can take zero or more parameters
def is_a_party(apples, pizzas):
    # Returns True if you have enough apples and pizzas to make a party happen
    if apples > 10 and pizzas > 10:
        return True
    else:
        return False


print(is_a_party(20, 20))


# A function with zero parameters
def throw_party():
    num_apples = int(input("How many apples do you have? "))
    num_pizzas = int(input("How many pizzas do you have? "))

    # Ask if this is enough for a party
    if is_a_party(num_apples, num_pizzas):
        return "Dude let's party down"
    else:
        return "You'll have to go to the store first."


print(throw_party())


# Recursion
def countdown(number):
    if number <= 0:
        print('Blastoff!')
    else:
        print(number)
        countdown(number - 1)


countdown(10)


def fib(n):
    global numCalls
    numCalls += 1
    print('fib called with', n)
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


numCalls = 0
n = 6
res = fib(n)
print('fib n=:', n, 'res:', res, 'numCalls:', numCalls)


def fastFib(n, memo):
    global numCalls
    numCalls += 1
    print('fib1 called with', n)
    if not n in memo:
        memo[n] = fastFib(n - 1, memo) + fastFib(n - 2, memo)
    return memo[n]


memo = {0: 1, 1: 1}
numCalls = 0
n = 6
res = fastFib(n, memo)
print('fib n=:', n, 'res:', res, 'numCalls:', numCalls)


# coding:UTF-8
# 前向引用
# best practice to put callee before caller.
def foo():
    print('in foo()')
    bar5()


# foo()  #will throw SyntaxError here

def bar5():
    print('in bar5()')


foo()  # will function well, becaue while call foo() here, bar5() already declared.

####内部函数 && 函数装饰器decorator
# 装饰器的作用: a) 引入日志 b) 计时逻辑，检测性能，c)加入事务的能力
from time import ctime, sleep


def tsfunc(func):
    print("test")

    def wrappedFunc():  # 内部函数
        print('[%s %s() called]' % (ctime(), func.__name__))
        return func()

    return wrappedFunc


@tsfunc  # 装饰器
def decoratedfun():
    pass


# testing code
decoratedfun()
sleep(4)
# testing code
for i in range(2):
    sleep(1)
    decoratedfun()


# 装饰器
def decorator(F):
    def new_function(x, y):
        print("input:", x, y)
        return F(x, y)

    return new_function


@decorator
def add(x, y):
    return x + y


@decorator
def multiply(x, y):
    return x * y


# testing code
print(add(2, 3))
print(multiply(2, 3))


# 函数作为参数传递
def convert(func, seq):
    'Convert sequence of numbers to same specifc type'
    return [func(eachNum) for eachNum in seq]


myseq = (123, 45.67)
print(convert(int, myseq))
print(convert(float, myseq))


# 函数默认参数
# Note:必要参数都要在默认参数之前
def defaultArgumentFunc(cost, rate=0.0825):
    'demo for function with default argument'
    return cost + cost * rate


# demo
defaultArgumentFunc(100)
defaultArgumentFunc(100, 0.05)


###非关键字可变长参数 tuple
def tupleVarArgs(arg1, arg2='defaultB', *theRest):  # * 号开头
    'display regular args and non-keyword variable args'
    print('formal arg 1:', arg1)
    print('formal arg 2:', arg2)
    for eachxtrArg in theRest:
        print('another arg:', eachxtrArg)


tupleVarArgs('abc')
tupleVarArgs(12, 4.56)
tupleVarArgs('xyz', 'cde', '123', 'test')


###关键字变量参数 dict
def dictVarArgs(arg1, arg2='defaultB', **theRest):  # ** 号开头
    'display regular args and keyword variable args'
    print('formal arg 1:', arg1)
    print('formal arg 2:', arg2)
    for eachxtrArg in theRest:
        print('xtra arg %s: %s' % \
              (eachxtrArg, str(theRest[eachxtrArg])))


dictVarArgs('abc')
dictVarArgs(12, 4.56)
dictVarArgs('xyz', 'cde', c='zoo', d='test')
dictVarArgs('xyz', 'cde', c='zoo', d='test', e=('a', 'b'))
atuple = ('a', 'b')
dictVarArgs('xyz', 'cde', **{'c': 10, 'd': 'test', 'e': atuple})


# 嵌套作用域
def topScope():
    a = 3

    def middleScope():
        b = 4
        print(a + b)

        def bottomScope():
            c = 5
            print(a + b + c)

        bottomScope()

    print(a)
    middleScope()


topScope()


# 闭包
# 如果在一个函数内部，对在外部作用域（但不是全局作用域）的变量
# 进行引用，那么内部函数就被认为是闭包(closure)。
# 定义在外部函数但是由内部函数引用或者使用的变量被称为自由变量。

# 函数闭包（function closures），是引用了自由变量的函数。这个被引用的自由变量将和这个函数一同存在，
# 即使已经离开了创造它的环境也不例外。
# 所以，有另一种说法认为闭包是由函数和与其相关的引用环境组合而成的实体。
def counter(start_at=0):
    count = [start_at]

    def incr():
        count[0] += 1
        return count[0]

    return incr


count = counter(5)
print(count())  # 6
print(count())  # 7

# 匿名函数
# python 中使用lambda表达式实现匿名函数
# 实际效果与下面的f(x)函数一致
g = lambda x: x ** 2
print(g(4))


def f(x):
    return x ** 2


print(f(4))

iterable = [1, 2, 3, 4]
result = map(g, iterable)
print(type(result))
print(result)

add = lambda x, y: x + y

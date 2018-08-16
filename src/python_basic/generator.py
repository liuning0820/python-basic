# 方法一: Generator Functions:
# generate a series of values (an iterable object) using yield statement.
def countdown(n):
    print("Counting down from ", n)
    while n > 0:
        yield n
        n -= 1


# Calling a generator function create a generator object. However, it does not start running the function.
# The function only executes on __next__()
x = countdown(5)
print(x)
for i in x:
    print(i)

# 方法二: Generator expressions:

s = [1, 2, 3, 4]
squares = (x * x for x in s)

print(squares)

for i in squares:
    print(i)

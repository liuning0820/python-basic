# input is a string unless converted
x = int(input("Give me a number:"))

# Chained conditionals
if x < 1:
    print("Too little")
elif 1 < x < 10:
    print("Just about right")
else:
    print("Too high")

# Alternative execution

if x % 2 == 0:
    print('x is even.')
else:
    print('x is odd.')

# Conditional expression:  make the above if statement more concisely.
print('x is even.') if x % 2 == 0 else print('x is odd.')

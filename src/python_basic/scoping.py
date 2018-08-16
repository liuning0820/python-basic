# adding x here makes it in scope
x = 0

for i in range(1, 10):
    # x is in scope
    x = i + x

# x is now out of scope
print(x)

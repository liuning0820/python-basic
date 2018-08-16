def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


classmates = ['michael', 'bob', 'Tracy']


# List comprehensions
# List comprehensions are concise and easy to read, at least for simple expressions. And they
# are usually faster than the equivalent for loops, sometimes much faster.
# But, in my defense, list comprehensions are harder to debug because you can’t put a print
# statement inside the loop. I suggest that you use them only if the computation is simple
# enough that you are likely to get it right the first time. And for beginners that means never.

def capitalize_all_v2(t):
    return [s.capitalize() for s in t]


print(capitalize_all(classmates))
print(capitalize_all_v2(classmates))

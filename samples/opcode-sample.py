import dis
def func():
    a = 10
    b = 20
    c = a + b
    return c

# load the module, and run below command in IDEL SHELL interactive
# >>> dis.dis(func)

#   3           0 LOAD_CONST               1 (10)
#               2 STORE_FAST               0 (a)

#   4           4 LOAD_CONST               2 (20)
#               6 STORE_FAST               1 (b)

#   5           8 LOAD_FAST                0 (a)
#              10 LOAD_FAST                1 (b)
#              12 BINARY_ADD
#              14 STORE_FAST               2 (c)

#   6          16 LOAD_FAST                2 (c)
#              18 RETURN_VALUE

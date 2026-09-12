a = '123е'
b = '91.4'
# c = 524.345 ** 435345345311145345  OverflowError: (34, 'Math result not representable')
d = '7.1 + 4'
# e = '4' - 2  TypeError: unsupported operand type(s) for -: 'str' and 'int'
f = '4 - 2'
g = '42'
h = -12.12

# print(int(a)) ValueError: invalid literal for int() with base 10: '123е'
# print(int(b))  ValueError: invalid literal for int() with base 10: '91.4'
# print(int(c))
# print(int(d))  ValueError: invalid literal for int() with base 10: '7.1 + 4'
# print(int(e))
# print(int(f))  ValueError: invalid literal for int() with base 10: '4 - 2'
print(int(g))
print(int(h))

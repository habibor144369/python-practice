# variable exchanging---
x = 20
y = 30
z = 40
def my_func(x, y, z = 10 ):
    print('x =', x, 'y =', y, 'z =', z)

my_func(x, y, z)
a = z
b = x
my_func(x = a, y = b)
x = a
y = y
my_func(x, y,)


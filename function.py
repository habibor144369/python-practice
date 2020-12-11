# local and global variable er example-----
def my_function(x):
    print('Inside my function', x)
    x = 10
    print('Inside my function', x)

x = 30
my_function(x)
print('This is my out side function', x)

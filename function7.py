#assing new ellements in list----
def my_func(li):
    li[0] = 10

my_list = [1, 2, 3, 4]
print('before function call', my_list)

my_func(my_list)
print('after function call', my_list)

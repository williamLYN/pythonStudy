my_tuple = (8, 12, 15, 21, 13, 9)
my_dict = {'num1': 4, 'num2': 5, 'num3': 20}


def tuple_func(tuple_parameter):
    for i in tuple_parameter:
        print(i)


def dict_func(dict_parameter):
    for key, value in dict_parameter.items():
        print(key, value)


tuple_func(my_tuple)
dict_func(my_dict)


def func01():
    print('func01执行了')
    return 100


print(func01())
res = func01()
func01()
print(res)

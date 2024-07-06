# str_input = input("拿的什么")
#
# if str_input == '定海神针':
#     print('是真的')
# else:
#     print('是假的')
#
# a = input('输入一个整数：')
#
# if int(a) % 3 == 0:
#     print('是三的倍数')
# else:
#     print('不是三的倍数')


num = int(input("输入成绩"))

if 100 >= num >= 90:
    print("优秀")
elif 89 >= num >= 80:
    print("良好")
elif 79 >= num >= 60:
    print("及格")
elif 59 >= num >= 0:
    print("不及格")
else:
    print("输入有误")

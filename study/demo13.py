# def chair_func(all_money, chair_price):
#     chair_number = all_money // chair_price // 10
#     res_money = all_money % (chair_price * 10)
#     return chair_number, res_money
#
#
# money = 30000
# price = 620
# number, res_amount = chair_func(money, price)
#
# print(f'公司采购{number * 10:^10}办公椅，公司剩余的钱数{res_amount:^10}元')


def test_fun(ma_fun, ca_fun):
    iq = ma_fun / ca_fun * 100
    if iq >= 140:
        return "天才"
    elif iq >= 120:
        return "超常"
    elif iq >= 110:
        return "聪慧"
    elif iq >= 90:
        return "正常"
    elif iq >= 80:
        return "迟钝"
    else:
        return "低能"


ma = int(input("请输入你的心里年龄:"))
ca = int(input("请输入你的实际年龄:"))

print(test_fun(ma, ca))

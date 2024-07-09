num_list = [8, 5, 7, 2, 9, 4, 3, 1, 6]
print(max(num_list))
print(min(num_list))
print(sum(num_list))
print(6 in num_list)


# 练习1:
# 唐僧西出大唐取经，创建一个列表表示西行路上的人。路上先后收服了孙悟空，猪八戒，沙僧和白龙马，请把四人添加到列表里面
# 练习2:
# 班级成绩如下:
# 现在班里来了两个插班生，考试的成绩分别是97，83请把他们的成绩插入到合适的位置

xiyou_list = ['唐僧']
xiyou_list.append('孙悟空')
xiyou_list.append('猪八戒')
xiyou_list.append('沙僧')
xiyou_list.append('白龙马')
print(xiyou_list)

scores = [100, 98, 96, 95, 93, 90, 85, 80, 66]
scores.insert(2, 97)
scores.insert(8, 83)
print(scores)

shopping_list1 = ['洁面乳', '深度学习', '4K显示屏', '口红']
shopping_list1.pop(0)
shopping_list1.pop(0)
print(shopping_list1)

shopping_list2 = ['洁面乳', '深度学习', '4K显示屏', '口红']
shopping_list2.remove('洁面乳')
shopping_list2.remove('深度学习')
print(shopping_list2)

scores = [92, 83, 100, 58, 73, 42]
for i in range(len(scores)):
    if (scores[i]) < 60:
        scores[i] = '不及格'
print(scores)


# 练习1:超市甩卖，原本的价格直接打八折，帮助小花同学修改购物车中的商品价格;并计算总价格，以及总优惠综合练习:
prices = [56, 120, 20, 100]
# 原来的总格
prices_count_last = 0
for i in prices:
    prices_count_last += i
print('总价' + str(prices_count_last))
# 折扣后商品价格
for i in range(len(prices)):
    prices[i] *= 0.8
print(prices)
# 折扣后总价格
prices_count_now = 0
for i in prices:
    prices_count_now += i
print('折扣后总价' + str(round(prices_count_now, 2)))

print('优惠价格' + str(round(prices_count_last - prices_count_now, 2)))

# 车辆在4S店前排队等服务，如下是在排车辆的品牌:请完成如下任务:
# 1.到 奥迪A6的号了，司机开车进入服务中心
# 2.新来了一辆'小康'的车，又新来一辆"保时捷911'
# 3.轮到宝马车主进场，又新来一辆'毒药'插队到奔驰前面
# 4.大众车主有点事，直接退出队伍
# 5.打印现在所有在排队的车子
cars = ['奥迪A6', '宝马530', '奔驰C', '大众迈腾', '米时捷']
cars.pop(0)
cars.append('小康')
cars.append('保时捷911')
cars.pop(0)
cars.insert(0, '毒药')
cars.remove('大众迈腾')
print(cars)

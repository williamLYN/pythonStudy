# 请设计一个二手房管理系统，要求建立两个模型，二手房以及二手房数据库
# 对于二手房，需要知道它的位置，每平售价，房屋面积，楼层，最近地铁距离，房屋总价信息。#对于数据库，可以使用列表，
# 要求可以增加、删除、更新和查看二手房信息，并且可以实现二手房信息遍历
class House:

    def __init__(self, location, price, area, floor, distance_to_subway, total_price):
        self.location = location
        self.price = price
        self.area = area
        self.floor = floor
        self.distance_to_subway = distance_to_subway
        self.total_price = total_price

    def display(self):
        print(f'Location:,{self.location}')
        print(f'Price:,{self.price}')
        print(f'Area:,{self.area}')
        print(f'Floor:,{self.floor}')
        print(f'Distance to subway:,{self.distance_to_subway}')
        print(f'Total price:,{self.total_price}')


class Database:

    def __init__(self):
        self.houses = []

    def add_house(self, house):
        self.houses.append(house)

    def delete_house(self, house):
        self.houses.remove(house)

    def update_house(self, house):
        for i in range(len(self.houses)):
            if self.houses[i] == house:
                self.houses[i] = house
                print('house update Successful')
            else:
                print('house update Failed')

    def get_houses(self):
        print(self.houses)





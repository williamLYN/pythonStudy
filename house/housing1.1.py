#把上述内容，按照MVC模式进行设计
#先去掉打印相关的内容，把他们放到View里面。定义用来打印和展示模型信息的方法
#在进行房屋修改和删除时，发现没有合适的房屋专属名称，于是增加一个ID编号
#添加Controller类，用来调用View和Model里面的方法和属性，以及修改

class House:
    def __init__(self, ID, location, price, area, floor, distance_to_subway, total_price):
        self.ID = ID
        self.location = location
        self.price = price
        self.area = area
        self.floor = floor
        self.distance_to_subway = distance_to_subway
        self.total_price = total_price

    def modefy_price(self, price):
        self.price = price
        self.total_price = self.price * self.area

    def display(self):
        return f'ID:{self.ID} location:{self.location} price:{self.price} area:{self.area} floor:{self.floor} distance_to_subway:{self.distance_to_subway} total_price:{self.total_price} '


class Database:

    def __init__(self):
        self.houses = []

    def add_house(self, house):
        self.houses.append(house)

    def delete_house(self, house):
        self.houses.remove(house)

    def update_house(self, house, new_house):
        i = self.houses.index(house)
        self.houses[i] = new_house

    def get_houses(self):
        return self.houses


class View:

    def __init__(self, db: Database):
        self.db = db

    def choice(self):
        text = '''
        1.add house
        2.delete house
        3.modify house
        4.display house
        5.exit
        '''
        print(text)
        choice = int(input('please input your choice:'))
        if choice in range(1, 6):
            return choice
        else:
            print('输入错误请重新输入')

    def display_houses(self):
        for house in self.db.houses:
            res = house.display()
            print(res)

    def display_info(self, message):
        print(message)


class Controller:
    def __init__(self, db: Database, view: View):
        self.db = db
        self.view = view

    def handle_input(self):
        choice = self.view.choice()
        if choice == 1:
            self.add_house()
        elif choice == 2:
            self.delete_house()
        elif choice == 3:
            self.update_house()
        elif choice == 4:
            self.view.display_houses()
        elif choice == 5:
            self.exit()

    def add_house(self):
        ID = int(input('please input ID:'))
        location = input('please input location:')
        price = float(input('please input price:'))
        area = float(input('please input area:'))
        floor = int(input('please input floor:'))
        distance_to_subway = float(input('please input distance_to_subway:'))
        total_price = price * area
        house = House(ID, location, price, area, floor, distance_to_subway, total_price)
        self.db.add_house(house)
        self.view.display_info('add house success')

    def delete_house(self):
        ID = int(input('请输入ID'))
        for house in self.db.houses:
            if house.ID == ID:
                self.db.delete_house(house)
                self.view.display_info('delete house success')
                return
        self.view.display_info('delete house fail')

    def update_house(self):
        ID = int(input('请输入ID'))
        for house in self.db.houses:
            if house.ID == ID:
                new_price = float(input('请输入新的价格'))
                house.modefy_price(new_price)
                self.view.display_info('update house success')
                return
        self.view.display_info('update house fail')

    def visit_houses(self):
        ID = int(input('请输入ID'))
        for house in self.db.houses:
            if house.ID == ID:
                self.view.display_info(house.display())
                return
        self.view.display_info('visit house fail')

    def display_houses(self):
        pass


if __name__ == '__main__':
    db = Database()
    view = View(db)
    controller = Controller(db, view)
    while True:
        controller.handle_input()

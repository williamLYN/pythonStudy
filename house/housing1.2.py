import sys
import json
import pickle


class House:
    def __init__(self, ID, location, price, area, floor_num, distance_to_subway, total_price):
        self.ID = ID
        self.location = location
        self.price = price
        self.area = area
        self.floor = floor_num
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

    def add_house_with_dict(self, data):
        for info in data:
            house = House(**info)
            self.houses.append(house)

    def add_house_with_list(self, data):
        for info in data:
            house = House(*info)
            self.houses.append(house)


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
    def __init__(self, database: Database, view: View):
        self.db = database
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

    def exit(self):
        sys.exit()


if __name__ == '__main__':
    db = Database()
    with open('houses.json', 'r', encoding='GBK') as f:
        data = json.load(f)
    db.add_house_with_dict(data)
    with open('houses.csv', 'r', encoding='GBK') as f:
        data = pickle.load(f)
    db.add_house_with_list(data)
    view = View(db)
    controller = Controller(db, view)
    while True:
        controller.handle_input()

import sys


class Product:

    # 初始化是指仅在创建的时候，进行一次性赋值
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


class ShoppingCart:
    def _init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def list_products(self):
        return self.products


class View:
    def get_user_choice(self):
        text = ''
        while True:
            print(text)
            case = input('请输入你要选择的功能(1-4,输入0退出)：')
            if case == '1':
                print('请添加商品')
                return 1
            elif case == '2':
                print('请删除商品')
                return 2
            elif case == '3':
                print('查看购物车清单')
                return 3
            elif case == '4':
                print('计算购物车总金额')
                return 4
            elif case == '0':
                return 0
            else:
                print('你的输入有误，请重新输入')

    def display_message(self, message):
        print(message)

    def display_products(self, info: Product):
        print(f'{info.name}商品的数量是{info.amount},单价是{info.price}')


class Controller:
    def __init__(self, view: View, model: ShoppingCart):
        self.view = view
        self.model = model

    # 在方法里面传入实例：有什么问题？
    # 每一次涉及到实例的时候，都需要传入一个view，不方便我们敲代码
    def handle_input(self):
        choice = self.view.get_user_choice()
        if choice == 1:
            self.add()
        elif choice == 2:
            self.delete()
        elif choice == 3:
            self.show()
        elif choice == 4:
            self.cal()
        elif choice == 0:
            sys.exit()

    def add(self):
        name = input('请输入商品名称：')
        price = float(input('请输入商品价格：'))
        amount = int(input('请输入购买数量：'))
        product = Product(name, price, amount)
        self.model.add_product(product)
        self.view.display_message(f'商品{product.name}已经成功添加到购物车')

    def delete(self):
        name = input('请输入要删除的商品名称：')
        for i in self.model.products:
            if i.name == name:
                self.model.remove_product(i)
                self.view.display_message(f'已经移除{i.name}商品')
                return
        self.view.display_message(f'{name}不在购物车里面')

    def show(self):
        product_list = self.model.list_products()
        if product_list:
            for i in product_list:
                self.view.display_products(i)
        else:
            self.view.display_message('购物车为空。')

    def cal(self):
        total_cash = self.model.total_cash()
        self.view.display_message(f'购物车总金额：{total_cash}')

    def update(self, flag):
        if flag == 1:
            name = input('请输入要删除的商品名称：')
            for i in self.model.products:
                if i.name == name:
                    self.model.remove_product(i)
                    self.view.display_message(f'已经移除{i.name}商品')
                    return
            self.view.display_message(f'{name}不在购物车里面')
        else:
            name = input('请输入商品名称：')
            price = float(input('请输入商品价格：'))
            amount = int(input('请输入购买数量：'))
            product = Product(name, price, amount)
            self.model.add_product(product)
            self.view.display_message(f'商品{product.name}已经成功添加到购物车')


cart = ShoppingCart()
view = View()
controller = Controller(view, cart)
while True:
    controller.handle_input()

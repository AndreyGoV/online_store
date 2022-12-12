import re


class Phone:
    def __init__(self, name, price, place_of_manufacture, count):
        self.name = name
        self.price = price
        self.place_of_manufacture = place_of_manufacture
        self.count = count

    def info(self):
        print(f'Модель - {self.name}\nЦена - {self.price}\nСтрана производства - {self.place_of_manufacture}')


class Shopping_bag(Phone):
    def __init__(self, status):
        self.status = 0
        self.total = 0
        self.list = []

    def add_goods(self, phone):
        if phone.count >= 1:
            self.status += 1
            self.list.append(phone.name)
            search = re.findall(r'\d+', phone.price)
            result = int(search[0])
            self.total += result
        else:
            print('Товара нет в наличии')

    def del_goods(self, phone):
        self.status -= 1
        self.list.remove(phone.name)
        search = re.findall(r'\d+', phone.price)
        result = int(search[0])
        self.total -= result

    def clear(self):
        self.list.clear()
        self.total = 0

    def get_goods(self):
        return self.list

    def total_price(self):
        return f'{self.total} рублей'


class Customer(Shopping_bag, Phone):
    def __init__(self, name):
        self.name = name
        self.count_goods = 0
        self.list_goods = []
        self.spend = 0

    def buy(self, phone):
        if phone.count >= 1:
            self.count_goods += 1
            self.list_goods.append(phone.name)
            search = re.findall(r'\d+', phone.price)
            result = int(search[0])
            self.spend += result
            phone.count -= 1
        else:
            print('Товара нет в наличии')

    def get_count(self):
        return self.count_goods

    def get_goods(self):
        return self.list_goods

    def get_total_spend(self):
        return self.spend


class Stock(Phone):
    def __init__(self):
        pass

    def add_goods(self, phone, amount):
        phone.count += amount



iphone_15 = Phone('Apple iPhone 15', '250000 рублей', 'Китай', 2)
nokia_3310 = Phone('Nokia 3310', '1000 рублей', 'Финляндия', 1)
samsung_K22 = Phone('Samsung K22', '120000 рублей', 'Северная Корея', 1)

shopping_bag = Shopping_bag(0)

customer1 = Customer('Иван')
customer2 = Customer('Василий')
customer3 = Customer('Стив')

stock = Stock()


# Просмотр информации о товаре
iphone_15.info()
samsung_K22.info()

# Работа с корзиной (добавить товар в корзину, удалить товар, посмотреть какие товары в корзине,
# очистить корзину, посмотреть общую стоимость выбранных товаров)
shopping_bag.add_goods(iphone_15)
shopping_bag.add_goods(nokia_3310)
shopping_bag.add_goods(samsung_K22)
print(shopping_bag.get_goods())
print(shopping_bag.total_price())
shopping_bag.del_goods(samsung_K22)
print(shopping_bag.get_goods())
print(shopping_bag.total_price())
shopping_bag.clear()
print(shopping_bag.get_goods())

# Покупатель (покупает товар, просмотр сколько товаров купил и какие товары купил, сколько денег потратил)
customer1.buy(nokia_3310)
customer1.buy(samsung_K22)
print(customer1.get_count())
print(customer1.get_goods())
print(customer1.get_total_spend())

# Склад (добавляет товар)
print(iphone_15.count)  # 2 шт.
stock.add_goods(iphone_15, 10)
print(iphone_15.count)  # 12 шт.

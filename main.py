#                       Home Task Pro - 3

# Task 1
# Ресторан дает возможность сделать онлайн заказ блюд. Размер скидки по заказу зависит от карты лояльности клиента:
# Regular, Silver или Gold.
# Необходимо написать Python-скрипт, возвращающий стоимость сделанного заказа.
# Для реализации разных типов карт лояльности необходимо использовать наследование.
#
# Для реализации приложения может быть использован следующий шаблон
#
# class Discount:
#     def discount(self):
#         pass
#
#
# class RegularDiscount(Discount):
#     def discount(self):
#         pass
#
#
# class SilverDiscount(Discount):
#     def discount(self):
#         pass
#
#
# class GoldDiscount(Discount):
#     def discount(self):
#         pass
#
#
# class Client:
#     def __init__(self, name, discount):
#         self.name = name
#         self.discount = discount
#
#     def get_total_price(self, order):
#         pass


class Discount:
    def discount(self, total_price):
        return total_price


class RegularDiscount(Discount):
    def discount(self, total_price):
        return total_price * 0.95


class SilverDiscount(Discount):
    def discount(self, total_price):
        return total_price * 0.9


class GoldDiscount(Discount):
    def discount(self, total_price):
        return total_price * 0.85


class Client:
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        total_price = sum(order.values())
        return self.discount.discount(total_price)


order = {'чай': 100, 'кофе': 200, 'пирожное': 300}

client1 = Client('Вася', RegularDiscount())
client2 = Client('Петя', SilverDiscount())
client3 = Client('Коля', GoldDiscount())

print(client1.get_total_price(order))
print(client2.get_total_price(order))
print(client3.get_total_price(order))


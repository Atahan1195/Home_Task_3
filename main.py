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
    """
    Базовый класс для скидок
    """
    def discount(self, total_price):
        """
        Метод для расчета скидки
        :param total_price: общая стоимость заказа
        :return: стоимость заказа со скидкой
        """
        return total_price


class RegularDiscount(Discount):
    """
    Класс для скидки по карте Regular
    """
    def discount(self, total_price):
        """
        Метод для расчета скидки
        :param total_price: общая стоимость заказа
        :return: стоимость заказа со скидкой 5%
        """
        return total_price * 0.95


class SilverDiscount(Discount):
    """
    Класс для скидки по карте Silver
    """
    def discount(self, total_price):
        """
        Метод для расчета скидки
        :param total_price: общая стоимость заказа
        :return: стоимость заказа со скидкой 10%
        """
        return total_price * 0.9


class GoldDiscount(Discount):
    """
    Класс для скидки по карте Gold
    """
    def discount(self, total_price):
        """
        Метод для расчета скидки
        :param total_price: общая стоимость заказа
        :return: стоимость заказа со скидкой 15%
        """
        return total_price * 0.85


class Client:
    """
    Класс для клиента
    """
    def __init__(self, name, discount):
        """
        Конструктор класса
        :param name: имя клиента
        :param discount: тип скидки
        """
        self.name = name
        self.discount = discount

    def get_total_price(self, order):
        """
        Метод для расчета стоимости заказа со скидкой
        :param order: заказ
        :return: стоимость заказа со скидкой
        """
        total_price = sum(order.values())
        return self.discount.discount(total_price)


regular_discount = Client('John', RegularDiscount())
silver_discount = Client('Bob', SilverDiscount())
gold_discount = Client('Atahan', GoldDiscount())

order = {'pizza': 100, 'cola': 50, 'french fries': 70}

print(f'Стоимость заказа со скидкой для клиента Regular: {regular_discount.get_total_price(order)}')
print(f'Стоимость заказа со скидкой для клиента Silver: {silver_discount.get_total_price(order)}')
print(f'Стоимость заказа со скидкой для клиента Gold: {gold_discount.get_total_price(order)}')

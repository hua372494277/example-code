from abc import  ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

"""
把Promotion定义为抽象基类 Abstract Base Class, ABC
为了使用@Abstractmentod装饰器，从而表明所用的模式
"""
class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """返回折扣金额>0"""


class FidelityPromo(Promotion):
    """积分>=1000的顾客提供5%折扣"""
    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion):
    """单个商品为20个及以上时提供10%折扣"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount

class LargeOrderPromo(Promotion):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    fidelityPromo_instance = Order(joe, cart, FidelityPromo())
    print(fidelityPromo_instance)
    fidelityPromo_instance = Order(ann, cart, FidelityPromo())
    print(fidelityPromo_instance)
    banana_cart = [LineItem('banan', 30, 0.5),
                   LineItem('apple', 10, 1.5)]
    print(Order(joe, banana_cart, BulkItemPromo()))
    long_order = [ LineItem(str(item_code), 1, 1.0)
                    for item_code in range(10) ]
    print(Order(joe, long_order, LargeOrderPromo()))
    print(Order(joe, cart, LargeOrderPromo()))
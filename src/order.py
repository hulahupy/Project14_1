from abc import ABC, abstractmethod

from src.product import Product


class BaseOrder(ABC):
    """Абстрактный базовый класс для заказа"""

    @abstractmethod
    def total_price(self) -> float:
        """Общая стоимость заказа"""
        pass


class Order(BaseOrder):
    """Класс для представления заказа"""

    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def total_price(self) -> float:
        """Общая стоимость заказа"""
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, {self.quantity} шт. на сумму {self.total_price()} руб."

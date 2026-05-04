from src.base_product import BaseProduct
from src.mixin import PrintInitMixin


class Product(BaseProduct, PrintInitMixin):
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        PrintInitMixin.print_init_info(self, name, description, price, quantity)
        super().__init__()

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: BaseProduct) -> float:
        """Сложение двух продуктов с проверкой типов"""
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать {type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity  # type: ignore[attr-defined]


class Smartphone(Product):
    """Класс для представления смартфона"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        # Печатаем информацию со всеми аргументами
        PrintInitMixin.print_init_info(self, name, description, price, quantity, efficiency, model, memory, color)


class LawnGrass(Product):
    """Класс для представления газонной травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
        # Печатаем информацию со всеми аргументами
        PrintInitMixin.print_init_info(self, name, description, price, quantity, country, germination_period, color)

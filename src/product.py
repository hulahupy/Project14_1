from src.base_product import BaseProduct
from src.mixin import PrintInitMixin


class Product(PrintInitMixin, BaseProduct):
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int, **kwargs):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity, **kwargs)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: BaseProduct) -> float:
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
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            efficiency=efficiency,
            model=model,
            memory=memory,
            color=color,
        )


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
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            country=country,
            germination_period=germination_period,
            color=color,
        )

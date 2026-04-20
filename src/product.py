class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой, что цена не отрицательная и не ноль"""
        if value <= 0:
            print("Цена не может быть отрицательной или нулевой")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        """Класс-метод для создания продукта из словаря"""
        return cls(
            name=product_dict["name"],
            description=product_dict["description"],
            price=product_dict["price"],
            quantity=product_dict["quantity"],
        )

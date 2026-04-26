class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое представление продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Сложение двух продуктов: общая стоимость товаров на складе"""
        if not isinstance(other, Product):
            raise TypeError(f"Нельзя сложить Product и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity

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
        """Сеттер для цены с проверкой"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self._price:
            # Дополнительное задание: подтверждение при понижении цены
            answer = input(f"Цена понижается с {self._price} до {value}. Подтвердите (y/n): ")
            if answer.lower() == "y":
                self._price = value
            else:
                print("Изменение цены отменено")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_dict: dict, existing_products: list = None) -> "Product":
        """Класс-метод для создания продукта из словаря с проверкой дубликатов"""
        name = product_dict["name"]
        description = product_dict["description"]
        price = product_dict["price"]
        quantity = product_dict["quantity"]

        if existing_products is not None:
            for existing in existing_products:
                if existing.name == name:
                    # Суммируем количество
                    existing.quantity += quantity
                    # Выбираем максимальную цену
                    if price > existing.price:
                        existing.price = price
                    return existing

        return cls(name, description, price, quantity)

class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # ← ИСПРАВЛЕНО: два подчёркивания
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price  # ← ИСПРАВЛЕНО: обращение к __price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены с проверкой"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:  # ← ИСПРАВЛЕНО: обращение к __price
            # Дополнительное задание: подтверждение при понижении цены
            answer = input(f"Цена понижается с {self.__price} до {value}. Подтвердите (y/n): ")
            if answer.lower() == "y":
                self.__price = value  # ← ИСПРАВЛЕНО
            else:
                print("Изменение цены отменено")
        else:
            self.__price = value  # ← ИСПРАВЛЕНО

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
                    # Выбираем максимальную цену (используем геттер и сеттер)
                    if price > existing.price:
                        existing.price = price
                    return existing

        return cls(name, description, price, quantity)

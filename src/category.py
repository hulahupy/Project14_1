from src.product import Product


class Category:
    """Класс для представления категории товаров"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> list[Product]:
        """Геттер для получения списка продуктов"""
        return self.__products

    def __str__(self) -> str:
        """Строковое представление категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавление продукта в категорию с проверкой типа"""
        if not isinstance(product, Product):
            raise TypeError(
                f"Можно добавлять только объекты Product или его наследников. Получен: {type(product).__name__}"
            )
        self.__products.append(product)
        Category.product_count += 1

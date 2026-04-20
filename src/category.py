from src.product import Product


class Category:
    """Класс для представления категории товаров"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут

        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> str:
        """Геттер для приватного атрибута products (возвращает строку)"""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result.strip()

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию"""
        self.__products.append(product)
        Category.product_count += 1

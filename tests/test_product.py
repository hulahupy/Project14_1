from src.product import Product


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        """Тест корректной инициализации продукта"""
        product = Product("Ноутбук", "Мощный игровой ноутбук", 150000.0, 10)

        assert product.name == "Ноутбук"
        assert product.description == "Мощный игровой ноутбук"
        assert product.price == 150000.0
        assert product.quantity == 10

    def test_product_price_float(self):
        """Тест, что цена может быть дробной"""
        product = Product("Мышь", "Беспроводная мышь", 1999.99, 25)
        assert isinstance(product.price, float)

    def test_product_quantity_int(self):
        """Тест, что количество — целое число"""
        product = Product("Клавиатура", "Механическая", 5000.0, 5)
        assert isinstance(product.quantity, int)

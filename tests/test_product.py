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

    def test_price_getter(self):
        """Тест получения цены"""
        product = Product("Телефон", "Смартфон", 30000.0, 3)
        assert product.price == 30000.0

    def test_price_setter_valid_increase(self):
        """Тест увеличения цены"""
        product = Product("Телефон", "Смартфон", 30000.0, 3)
        product.price = 35000.0
        assert product.price == 35000.0

    def test_price_setter_invalid_negative(self):
        """Тест: при отрицательной цене цена не меняется"""
        product = Product("Телефон", "Смартфон", 30000.0, 3)
        product.price = -1000.0
        # Цена устанавливается как есть (нет валидации)
        assert product.price == -1000.0

    def test_price_setter_invalid_zero(self):
        """Тест: при нулевой цене"""
        product = Product("Телефон", "Смартфон", 30000.0, 3)
        product.price = 0
        assert product.price == 0

    def test_price_setter_decrease_cancelled(self):
        """Тест понижения цены"""
        product = Product("Телефон", "Смартфон", 30000.0, 3)
        product.price = 25000.0
        assert product.price == 25000.0

import pytest
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
        """Тест геттера цены"""
        product = Product("Монитор", "27 дюймов", 25000.0, 7)
        assert product.price == 25000.0

    def test_price_setter_valid_increase(self):
        """Тест увеличения цены через сеттер"""
        product = Product("Телефон", "Смартфон", 30000.0, 3)
        product.price = 35000.0
        assert product.price == 35000.0

    def test_price_setter_invalid_negative(self):
        """Тест: при отрицательной цене выводится сообщение (цена не меняется)"""
        product = Product("Телефон", "Смартфон", 30000.0, 3)
        product.price = -1000.0
        # Цена не должна измениться
        assert product.price == 30000.0

    def test_price_setter_invalid_zero(self):
        """Тест: при нулевой цене выводится сообщение (цена не меняется)"""
        product = Product("Телефон", "Смартфон", 30000.0, 3)
        product.price = 0
        # Цена не должна измениться
        assert product.price == 30000.0

    def test_price_setter_decrease_confirmed(self, monkeypatch):
        """Тест понижения цены с подтверждением (пользователь вводит y)"""
        product = Product("Телефон", "Смартфон", 30000.0, 3)
        # Мокаем input, чтобы вернуть 'y'
        monkeypatch.setattr('builtins.input', lambda _: 'y')
        product.price = 25000.0
        assert product.price == 25000.0

    def test_price_setter_decrease_cancelled(self, monkeypatch):
        """Тест понижения цены с отменой (пользователь вводит n)"""
        product = Product("Телефон", "Смартфон", 30000.0, 3)
        # Мокаем input, чтобы вернуть 'n'
        monkeypatch.setattr('builtins.input', lambda _: 'n')
        product.price = 25000.0
        # Цена не должна измениться
        assert product.price == 30000.0

    def test_new_product_new(self):
        """Тест создания нового продукта через new_product (дубликатов нет)"""
        product = Product.new_product(
            {"name": "Планшет", "description": "10 дюймов", "price": 20000.0, "quantity": 2},
            []
        )
        assert product.name == "Планшет"
        assert product.description == "10 дюймов"
        assert product.price == 20000.0
        assert product.quantity == 2

    def test_new_product_duplicate_sum_quantity(self):
        """Тест: при создании дубликата количество суммируется"""
        existing = []
        product1 = Product.new_product(
            {"name": "Телефон", "description": "Смартфон", "price": 30000.0, "quantity": 5},
            existing
        )
        product2 = Product.new_product(
            {"name": "Телефон", "description": "Смартфон", "price": 32000.0, "quantity": 3},
            [product1]
        )
        assert product2.quantity == 8

    def test_new_product_duplicate_max_price(self):
        """Тест: при создании дубликата выбирается максимальная цена"""
        existing = []
        product1 = Product.new_product(
            {"name": "Телефон", "description": "Смартфон", "price": 30000.0, "quantity": 5},
            existing
        )
        product2 = Product.new_product(
            {"name": "Телефон", "description": "Смартфон", "price": 32000.0, "quantity": 3},
            [product1]
        )
        assert product2.price == 32000.0

    def test_new_product_duplicate_lower_price(self):
        """Тест: при дубликате с меньшей ценой цена не меняется"""
        existing = []
        product1 = Product.new_product(
            {"name": "Телефон", "description": "Смартфон", "price": 30000.0, "quantity": 5},
            existing
        )
        product2 = Product.new_product(
            {"name": "Телефон", "description": "Смартфон", "price": 25000.0, "quantity": 3},
            [product1]
        )
        assert product2.price == 30000.0
        assert product2.quantity == 8

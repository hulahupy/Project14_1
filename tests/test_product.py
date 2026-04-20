from src.product import Product


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        product = Product("Ноутбук", "Мощный игровой ноутбук", 150000.0, 10)
        assert product.name == "Ноутбук"
        assert product.description == "Мощный игровой ноутбук"
        assert product.price == 150000.0
        assert product.quantity == 10

    def test_product_price_float(self):
        product = Product("Мышь", "Беспроводная мышь", 1999.99, 25)
        assert isinstance(product.price, float)

    def test_product_quantity_int(self):
        product = Product("Клавиатура", "Механическая", 5000.0, 5)
        assert isinstance(product.quantity, int)

    def test_new_product_classmethod(self):
        product_data = {"name": "Телефон", "description": "Смартфон", "price": 25000.0, "quantity": 7}
        product = Product.new_product(product_data)
        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 25000.0
        assert product.quantity == 7

    def test_new_product_with_duplicate(self):
        """Тест: при дубликате товара количество суммируется, цена выбирается максимальная"""
        existing_product = Product("Телефон", "Описание", 1000.0, 5)
        existing_products = [existing_product]

        new_product_data = {"name": "Телефон", "description": "Новое описание", "price": 1200.0, "quantity": 3}

        result = Product.new_product(new_product_data, existing_products)
        assert result is existing_product
        assert result.quantity == 8
        assert result.price == 1200.0

    def test_new_product_with_duplicate_lower_price(self):
        """Тест: при дубликате с меньшей ценой — цена остаётся старой"""
        existing_product = Product("Телефон", "Описание", 1500.0, 5)
        existing_products = [existing_product]

        new_product_data = {"name": "Телефон", "description": "Новое описание", "price": 1200.0, "quantity": 3}

        result = Product.new_product(new_product_data, existing_products)
        assert result.quantity == 8
        assert result.price == 1500.0  # Цена не изменилась, так как была выше

    def test_price_setter_valid(self):
        product = Product("Товар", "Описание", 100.0, 5)
        product.price = 200.0
        assert product.price == 200.0

    def test_price_setter_invalid(self, capsys):
        product = Product("Товар", "Описание", 100.0, 5)
        product.price = -50
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0

        product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0

    def test_price_setter_decrease_confirmation(self, monkeypatch, capsys):
        """Тест: при понижении цены запрашивается подтверждение"""
        product = Product("Товар", "Описание", 100.0, 5)

        # Симулируем ввод 'y'
        monkeypatch.setattr("builtins.input", lambda _: "y")
        product.price = 80.0
        assert product.price == 80.0

        # Симулируем ввод 'n'
        monkeypatch.setattr("builtins.input", lambda _: "n")
        product.price = 60.0
        assert product.price == 80.0  # Не изменилась
        captured = capsys.readouterr()
        assert "Изменение цены отменено" in captured.out

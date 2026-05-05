from src.product import Product, Smartphone


class TestSmartphone:
    """Тесты для класса Smartphone"""

    def test_smartphone_initialization(self):
        """Тест инициализации смартфона"""
        phone = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        )

        assert phone.name == "Samsung Galaxy S23 Ultra"
        assert phone.description == "256GB, Серый цвет, 200MP камера"
        assert phone.price == 180000.0
        assert phone.quantity == 5
        assert phone.efficiency == 95.5
        assert phone.model == "S23 Ultra"
        assert phone.memory == 256
        assert phone.color == "Серый"

    def test_smartphone_inheritance(self):
        """Тест наследования от Product"""
        phone = Smartphone("Phone", "Desc", 1000.0, 10, 90.0, "Model", 128, "Black")
        assert isinstance(phone, Product)
        assert hasattr(phone, "name")
        assert hasattr(phone, "price")
        assert hasattr(phone, "quantity")

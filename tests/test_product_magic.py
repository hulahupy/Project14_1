import pytest

from src.product import Product


class TestProductMagic:
    """Тесты для магических методов Product"""

    def test_product_str(self):
        """Тест строкового представления продукта"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        expected = "Телефон, 50000.0 руб. Остаток: 10 шт."
        assert str(product) == expected

    def test_product_add(self):
        """Тест сложения продуктов (общая стоимость)"""
        p1 = Product("Товар 1", "Описание", 100.0, 10)  # 100 × 10 = 1000
        p2 = Product("Товар 2", "Описание", 200.0, 2)  # 200 × 2 = 400
        assert p1 + p2 == 1400.0

    def test_product_add_different_types(self):
        """Тест сложения с неправильным типом"""
        p1 = Product("Товар", "Описание", 100.0, 5)
        with pytest.raises(TypeError):
            _ = p1 + 100  # Нельзя сложить Product с числом

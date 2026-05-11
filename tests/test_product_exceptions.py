import pytest

from src.product import LawnGrass, Product, Smartphone


class TestProductExceptions:
    """Тесты для исключений в классе Product"""

    def test_product_zero_quantity_raises_error(self):
        """Тест: создание продукта с quantity=0 вызывает ValueError"""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("Бракованный товар", "Неверное количество", 1000.0, 0)

    def test_product_negative_quantity_raises_error(self):
        """Тест: создание продукта с отрицательным quantity вызывает ValueError"""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("Бракованный товар", "Отрицательное количество", 1000.0, -5)

    def test_product_valid_quantity_no_error(self):
        """Тест: создание продукта с положительным quantity не вызывает ошибку"""
        product = Product("Нормальный товар", "Описание", 1000.0, 10)
        assert product.quantity == 10

    def test_smartphone_valid_quantity_no_error(self):
        """Тест: создание смартфона с положительным quantity не вызывает ошибку"""
        phone = Smartphone("Phone", "Desc", 1000.0, 5, 95.0, "Model", 128, "Black")
        assert phone.quantity == 5

    def test_lawn_grass_valid_quantity_no_error(self):
        """Тест: создание травы с положительным quantity не вызывает ошибку"""
        grass = LawnGrass("Grass", "Desc", 100.0, 10, "USA", "5 days", "Green")
        assert grass.quantity == 10

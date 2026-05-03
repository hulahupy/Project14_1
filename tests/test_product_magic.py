import pytest

from src.product import LawnGrass, Product, Smartphone


class TestProductMagic:
    """Тесты для магических методов Product"""

    def test_product_str(self):
        """Тест строкового представления продукта"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        expected = "Телефон, 50000.0 руб. Остаток: 10 шт."
        assert str(product) == expected

    def test_product_add_same_type_product(self):
        """Тест сложения двух обычных продуктов"""
        p1 = Product("Товар 1", "Описание", 100.0, 10)
        p2 = Product("Товар 2", "Описание", 200.0, 2)
        assert p1 + p2 == 1400.0

    def test_product_add_same_type_smartphone(self):
        """Тест сложения двух смартфонов"""
        s1 = Smartphone("Phone1", "Desc", 1000.0, 5, 95.0, "Model1", 128, "Black")
        s2 = Smartphone("Phone2", "Desc", 2000.0, 3, 98.0, "Model2", 256, "White")
        result = s1 + s2
        assert result == 1000.0 * 5 + 2000.0 * 3

    def test_product_add_same_type_lawn_grass(self):
        """Тест сложения двух газонных трав"""
        g1 = LawnGrass("Grass1", "Desc", 100.0, 5, "USA", "5 days", "Green")
        g2 = LawnGrass("Grass2", "Desc", 200.0, 2, "Russia", "7 days", "Dark Green")
        result = g1 + g2
        assert result == 100.0 * 5 + 200.0 * 2

    def test_product_add_different_types_raises_error(self):
        """Тест: сложение разных типов вызывает TypeError"""
        smartphone = Smartphone("Phone", "Desc", 1000.0, 5, 95.0, "Model", 128, "Black")
        grass = LawnGrass("Grass", "Desc", 100.0, 10, "USA", "5 days", "Green")
        with pytest.raises(TypeError):
            _ = smartphone + grass

    def test_product_add_product_and_smartphone_raises_error(self):
        """Тест: сложение Product и Smartphone вызывает TypeError"""
        product = Product("Generic", "Desc", 500.0, 10)
        smartphone = Smartphone("Phone", "Desc", 1000.0, 5, 95.0, "Model", 128, "Black")
        with pytest.raises(TypeError):
            _ = product + smartphone

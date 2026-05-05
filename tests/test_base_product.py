import pytest

from src.base_product import BaseProduct
from src.product import LawnGrass, Product, Smartphone


class TestBaseProduct:
    """Тесты для абстрактного класса BaseProduct"""

    def test_base_product_abstract(self):
        """Тест, что BaseProduct - абстрактный класс"""
        with pytest.raises(TypeError):
            BaseProduct()  # Нельзя создать экземпляр абстрактного класса

    def test_product_inherits_from_base(self):
        """Тест, что Product наследует BaseProduct"""
        assert issubclass(Product, BaseProduct)

    def test_smartphone_inherits_from_base(self):
        """Тест, что Smartphone наследует BaseProduct"""
        assert issubclass(Smartphone, BaseProduct)

    def test_lawn_grass_inherits_from_base(self):
        """Тест, что LawnGrass наследует BaseProduct"""
        assert issubclass(LawnGrass, BaseProduct)

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


class TestProductIterator:
    """Тесты для итератора товаров"""

    def test_iterator(self):
        """Тест итерации по товарам категории"""
        p1 = Product("Товар 1", "Описание", 100.0, 5)
        p2 = Product("Товар 2", "Описание", 200.0, 3)
        category = Category("Категория", "Описание", [p1, p2])

        items = []
        for product in ProductIterator(category):
            items.append(product)

        assert len(items) == 2
        assert items[0].name == "Товар 1"
        assert items[1].name == "Товар 2"

    def test_iterator_empty(self):
        """Тест итерации по пустой категории"""
        category = Category("Пустая", "Нет товаров", [])
        items = list(ProductIterator(category))
        assert len(items) == 0

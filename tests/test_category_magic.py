from src.category import Category
from src.product import Product


class TestCategoryMagic:
    """Тесты для магических методов Category"""

    def test_category_str(self):
        """Тест строкового представления категории"""
        p1 = Product("Товар 1", "Описание", 100.0, 5)
        p2 = Product("Товар 2", "Описание", 200.0, 3)
        category = Category("Электроника", "Описание категории", [p1, p2])
        # Общее количество: 5 + 3 = 8
        expected = "Электроника, количество продуктов: 8 шт."
        assert str(category) == expected

    def test_category_str_empty_products(self):
        """Тест строкового представления пустой категории"""
        category = Category("Пустая", "Нет товаров", [])
        expected = "Пустая, количество продуктов: 0 шт."
        assert str(category) == expected

import pytest

from src.category import Category
from src.product import Product


class TestCategory:
    """Тесты для класса Category"""

    def setup_method(self):
        self.product1 = Product("Товар1", "Описание1", 100.0, 5)
        self.product2 = Product("Товар2", "Описание2", 200.0, 3)
        self.products = [self.product1, self.product2]

    def test_category_initialization(self):
        category = Category("Электроника", "Разные электронные устройства", self.products)
        assert category.name == "Электроника"
        assert category.description == "Разные электронные устройства"
        assert "Товар1" in category.products
        assert "Товар2" in category.products

    def test_category_count_increments(self):
        initial_count = Category.category_count
        Category("Новая категория", "Описание", [])
        assert Category.category_count == initial_count + 1

    def test_product_count_increments(self):
        initial_count = Category.product_count
        Category("Категория с товарами", "Описание", self.products)
        assert Category.product_count == initial_count + len(self.products)

    def test_add_product(self):
        category = Category("Тестовая категория", "Описание", [])
        initial_product_count = Category.product_count
        new_product = Product("Новый товар", "Описание", 500.0, 10)

        category.add_product(new_product)

        assert "Новый товар" in category.products
        assert Category.product_count == initial_product_count + 1

    def test_products_getter_format(self):
        category = Category("Электроника", "Описание", self.products)
        expected = "Товар1, 100.0 руб. Остаток: 5 шт.\nТовар2, 200.0 руб. Остаток: 3 шт."
        assert category.products == expected

    def test_products_getter_empty(self):
        category = Category("Пустая", "Описание", [])
        assert category.products == ""

    def test_products_private_attribute(self):
        category = Category("Электроника", "Описание", self.products)
        with pytest.raises(AttributeError):
            _ = category.__products

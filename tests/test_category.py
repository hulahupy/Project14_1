from src.category import Category
from src.product import Product


class TestCategory:
    """Тесты для класса Category"""

    def setup_method(self):
        """Подготовка тестовых данных"""
        self.product1 = Product("Товар1", "Описание1", 100.0, 5)
        self.product2 = Product("Товар2", "Описание2", 200.0, 3)
        self.products = [self.product1, self.product2]

    def test_category_initialization(self):
        """Тест корректной инициализации категории"""
        category = Category("Электроника", "Разные электронные устройства", self.products)

        assert category.name == "Электроника"
        assert category.description == "Разные электронные устройства"
        assert len(category.products) == 2
        # Проверяем, что товары в списке (по объектам, не по строкам)
        assert self.product1 in category.products
        assert self.product2 in category.products

    def test_category_count_increments(self):
        """Тест увеличения счетчика категорий"""
        initial_count = Category.category_count
        Category("Новая категория", "Описание", [])
        assert Category.category_count == initial_count + 1

    def test_product_count_increments(self):
        """Тест увеличения счетчика продуктов"""
        initial_count = Category.product_count
        Category("Категория с товарами", "Описание", self.products)
        assert Category.product_count == initial_count + len(self.products)

    def test_products_getter_format(self):
        """Тест строкового представления продуктов категории"""
        category = Category("Электроника", "Описание", self.products)
        # Проверяем, что products возвращает список объектов Product
        assert isinstance(category.products, list)
        assert len(category.products) == 2
        assert isinstance(category.products[0], Product)

    def test_products_getter_empty(self):
        """Тест пустой категории"""
        category = Category("Пустая", "Описание", [])
        assert category.products == []

    def test_products_private_attribute(self):
        """Тест, что продукты хранятся в приватном атрибуте"""
        category = Category("Тест", "Описание", self.products)
        # Проверяем, что есть защищённый атрибут
        assert hasattr(category, "_Category__products")

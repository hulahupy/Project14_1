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
        assert category.products[0] == self.product1

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

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


class TestCategoryMiddlePrice:
    """Тесты для метода middle_price в классе Category"""

    def test_middle_price_with_products(self):
        """Тест: средняя цена категории с товарами"""
        p1 = Product("Товар 1", "Описание", 100.0, 5)
        p2 = Product("Товар 2", "Описание", 200.0, 3)
        p3 = Product("Товар 3", "Описание", 300.0, 2)
        category = Category("Категория", "Описание", [p1, p2, p3])

        # Средняя цена: (100 + 200 + 300) / 3 = 200
        assert category.middle_price() == 200.0

    def test_middle_price_with_one_product(self):
        """Тест: средняя цена категории с одним товаром"""
        p1 = Product("Товар 1", "Описание", 150.0, 5)
        category = Category("Категория", "Описание", [p1])
        assert category.middle_price() == 150.0

    def test_middle_price_empty_category(self):
        """Тест: средняя цена пустой категории возвращает 0"""
        category = Category("Пустая категория", "Описание", [])
        assert category.middle_price() == 0.0

    def test_middle_price_with_smartphones(self):
        """Тест: средняя цена категории со смартфонами"""
        s1 = Smartphone("Phone1", "Desc", 1000.0, 5, 95.0, "Model1", 128, "Black")
        s2 = Smartphone("Phone2", "Desc", 2000.0, 3, 98.0, "Model2", 256, "White")
        category = Category("Смартфоны", "Описание", [s1, s2])

        # Средняя цена: (1000 + 2000) / 2 = 1500
        assert category.middle_price() == 1500.0

    def test_middle_price_with_lawn_grasses(self):
        """Тест: средняя цена категории с травой"""
        g1 = LawnGrass("Grass1", "Desc", 100.0, 5, "USA", "5 days", "Green")
        g2 = LawnGrass("Grass2", "Desc", 200.0, 3, "Russia", "7 days", "Dark Green")
        category = Category("Трава", "Описание", [g1, g2])

        # Средняя цена: (100 + 200) / 2 = 150
        assert category.middle_price() == 150.0

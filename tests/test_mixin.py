from src.product import LawnGrass, Product, Smartphone


class TestPrintInitMixin:
    """Тесты для миксина PrintInitMixin"""

    def test_product_print_init(self, capsys):
        """Тест вывода информации при создании Product"""
        Product("Телефон", "Смартфон", 50000.0, 10)
        captured = capsys.readouterr()
        assert "Product('Телефон', 'Смартфон', 50000.0, 10)" in captured.out

    def test_smartphone_print_init(self, capsys):
        """Тест вывода информации при создании Smartphone"""
        Smartphone("iPhone", "Смартфон", 100000.0, 5, 95.5, "15 Pro", 256, "Black")
        captured = capsys.readouterr()
        assert "Smartphone('iPhone', 'Смартфон', 100000.0, 5, 95.5, '15 Pro', 256, 'Black')" in captured.out

    def test_lawn_grass_print_init(self, capsys):
        """Тест вывода информации при создании LawnGrass"""
        LawnGrass("Трава", "Газонная", 500.0, 20, "Россия", "7 дней", "Зеленый")
        captured = capsys.readouterr()
        assert "LawnGrass('Трава', 'Газонная', 500.0, 20, 'Россия', '7 дней', 'Зеленый')" in captured.out

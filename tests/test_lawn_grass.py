from src.product import LawnGrass, Product


class TestLawnGrass:
    """Тесты для класса LawnGrass"""

    def test_lawn_grass_initialization(self):
        """Тест инициализации газонной травы"""
        grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

        assert grass.name == "Газонная трава"
        assert grass.description == "Элитная трава для газона"
        assert grass.price == 500.0
        assert grass.quantity == 20
        assert grass.country == "Россия"
        assert grass.germination_period == "7 дней"
        assert grass.color == "Зеленый"

    def test_lawn_grass_inheritance(self):
        """Тест наследования от Product"""
        grass = LawnGrass("Grass", "Desc", 100.0, 5, "USA", "5 days", "Green")
        assert isinstance(grass, Product)
        assert hasattr(grass, "name")
        assert hasattr(grass, "price")
        assert hasattr(grass, "quantity")

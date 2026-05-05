from src.order import Order
from src.product import Product


class TestOrder:
    """Тесты для класса Order"""

    def test_order_initialization(self):
        """Тест инициализации заказа"""
        product = Product("Товар", "Описание", 1000.0, 10)
        order = Order(product, 3)
        assert order.product == product
        assert order.quantity == 3

    def test_order_total_price(self):
        """Тест расчёта общей стоимости заказа"""
        product = Product("Товар", "Описание", 1000.0, 10)
        order = Order(product, 3)
        assert order.total_price() == 3000.0

    def test_order_str(self):
        """Тест строкового представления заказа"""
        product = Product("Товар", "Описание", 1000.0, 10)
        order = Order(product, 3)
        expected = "Заказ: Товар, 3 шт. на сумму 3000.0 руб."
        assert str(order) == expected

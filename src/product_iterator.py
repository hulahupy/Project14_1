from src.category import Category
from src.product import Product


class ProductIterator:
    """Класс для итерации по товарам категории"""

    def __init__(self, category: Category):
        self.category = category
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self) -> Product:
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        raise StopIteration

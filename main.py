from src.category import Category
from src.product import Product

if __name__ == "__main__":
    # Создаём продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаём категорию с продуктами
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных " "функций для удобства жизни",
        [product1, product2, product3],
    )

    # Выводим список продуктов в категории
    print("Продукты в категории:", category1.products)

    # Создаём новый продукт и добавляем его в категорию
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    # Выводим обновлённый список продуктов и количество товаров
    print("Продукты после добавления:", category1.products)
    print("Количество товаров в категории:", category1.product_count)

    # Создаём продукт через класс-метод new_product из словаря
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    # Меняем цену через сеттер (корректное значение)
    new_product.price = 800
    print("Цена после установки 800:", new_product.price)

    # Пытаемся установить некорректную цену (отрицательную)
    new_product.price = -100
    print("Цена после попытки установить -100:", new_product.price)

    # Пытаемся установить некорректную цену (ноль)
    new_product.price = 0
    print("Цена после попытки установить 0:", new_product.price)

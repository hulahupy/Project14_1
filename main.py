from src.product import Product
from src.category import Category


if __name__ == '__main__':
    # Проверка исключения при создании продукта с нулевым количеством
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print("Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    # Создание нормальных продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создание категории
    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    # Вывод средней цены
    print(f"Средняя цена в категории 'Смартфоны': {category1.middle_price()}")

    # Проверка средней цены для пустой категории
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средняя цена в пустой категории: {category_empty.middle_price()}")

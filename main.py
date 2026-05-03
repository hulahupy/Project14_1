from src.product import Product, Smartphone, LawnGrass
from src.category import Category


if __name__ == '__main__':
    # Создаём смартфоны
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )
    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий"
    )

    # Выводим информацию о смартфонах
    print("=== Смартфоны ===")
    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)
    print()

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)
    print()

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)
    print()

    # Создаём газонную траву
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый"
    )

    # Выводим информацию о траве
    print("=== Газонная трава ===")
    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)
    print()

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(glass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)
    print()

    # Проверяем сложение (одинаковые типы)
    print("=== Сложение одинаковых типов ===")
    smartphone_sum = smartphone1 + smartphone2
    print(f"Сумма смартфонов: {smartphone_sum}")

    grass_sum = grass1 + grass2
    print(f"Сумма травы: {grass_sum}")
    print()

    # Проверяем сложение (разные типы — должна быть ошибка)
    print("=== Сложение разных типов ===")
    try:
        invalid_sum = smartphone1 + grass1
    except TypeError as e:
        print(f"Возникла ошибка TypeError: {e}")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")
    print()

    # Создаём категории
    category_smartphones = Category(
        "Смартфоны",
        "Высокотехнологичные смартфоны",
        [smartphone1, smartphone2]
    )
    category_grass = Category(
        "Газонная трава",
        "Различные виды газонной травы",
        [grass1, grass2]
    )

    # Добавляем третий смартфон в категорию
    category_smartphones.add_product(smartphone3)

    # Выводим товары в категории смартфонов
    print("=== Товары в категории 'Смартфоны' ===")
    for product in category_smartphones.products:
        print(f"  - {product}")
    print()

    print(f"Общее количество продуктов в системе: {Category.product_count}")
    print()

    # Проверяем добавление не-продукта
    print("=== Проверка добавления не-продукта ===")
    try:
        category_smartphones.add_product("Not a product")
    except TypeError as e:
        print(f"Возникла ошибка TypeError: {e}")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")

from src.category import Category
from src.json_loader import load_categories_from_json
from src.product import Product


def demo_manual_creation():
    """Демонстрация ручного создания объектов"""
    print("=" * 50)
    print("Ручное создание объектов")
    print("=" * 50)

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных " "функций для удобства жизни",
        [product1, product2, product3],
    )

    print(f"Категория: {category.name}")
    print(f"Товаров в категории: {len(category.products)}")
    for product in category.products:
        print(f"  - {product.name}: {product.price} ₽")


def demo_json_loading():
    """Демонстрация загрузки из JSON"""
    print("\n" + "=" * 50)
    print("Загрузка из JSON файла")
    print("=" * 50)

    categories = load_categories_from_json("products.json")

    print(f"Всего загружено категорий: {len(categories)}")
    print(f"Всего категорий в системе (атрибут класса): {Category.category_count}")
    print(f"Всего товаров в системе (атрибут класса): {Category.product_count}")
    print()

    for category in categories:
        print(f"📁 Категория: {category.name}")
        print(f"   Описание: {category.description}")
        print(f"   Товары ({len(category.products)}):")
        for product in category.products:
            print(f"     📦 {product.name} | {product.price} ₽ | {product.quantity} шт.")
        print()


if __name__ == "__main__":
    # Сброс счетчиков для чистоты демонстрации (только для показа)
    Category.category_count = 0
    Category.product_count = 0

    demo_manual_creation()
    demo_json_loading()

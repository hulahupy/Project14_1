# Project14_1 - Управление категориями и товарами

## Описание
Проект реализует систему управления товарами и категориями для интернет-магазина.  
Поддерживаются различные типы товаров: обычные продукты, смартфоны и газонная трава.

---

## Классы

### Product (базовый класс)
- `name` - название товара
- `description` - описание
- `price` - цена
- `quantity` - количество на складе

**Магические методы:**
- `__str__` - строковое представление: `"Название, X руб. Остаток: X шт."`
- `__add__` - сложение товаров (только одинаковых классов)

### Smartphone (наследник Product)
Дополнительные атрибуты:
- `efficiency` - производительность
- `model` - модель
- `memory` - объем встроенной памяти (ГБ)
- `color` - цвет

### LawnGrass (наследник Product)
Дополнительные атрибуты:
- `country` - страна-производитель
- `germination_period` - срок прорастания
- `color` - цвет

### Category
- `name` - название категории
- `description` - описание
- `products` - список товаров в категории (приватный атрибут)

**Атрибуты класса:**
- `category_count` - общее количество категорий
- `product_count` - общее количество товаров

**Методы:**
- `add_product()` - добавление товара в категорию (с проверкой типа)
- `__str__` - строковое представление: `"Название, количество продуктов: X шт."`

### ProductIterator
Класс для итерации по товарам категории в цикле `for`.

---

## Новое в этой версии

### Классы-наследники Product
- **Smartphone** - смартфоны с дополнительными характеристиками
- **LawnGrass** - газонная трава с дополнительными характеристиками

### Ограничения сложения
- Складывать можно только товары **одного класса**
- При попытке сложить разные классы (например, `Smartphone + LawnGrass`) выбрасывается `TypeError`
- Для проверки используется функция `type()`

### Безопасное добавление в категорию
- Метод `add_product` проверяет, что добавляется объект `Product` или его наследник
- При попытке добавить другой тип (строку, число и т.д.) выбрасывается `TypeError`
- Для проверки используется функция `isinstance()`

---

## Установка и запуск

### Требования
- Python 3.10+
- Poetry

### Установка зависимостей
```
poetry install
Запуск демонстрационного скрипта

poetry run python main.py
Тестирование
Запуск всех тестов

poetry run pytest -v
Проверка покрытия

poetry run pytest --cov=src --cov-report=term
Генерация HTML отчёта о покрытии

poetry run pytest --cov=src --cov-report=html
Отчёт сохраняется в папку htmlcov/.

Результаты тестирования
Всего тестов: 31

Покрытие кода: 100%

Линтеры и форматирование
Форматирование кода (Black)

poetry run black src/ tests/
Сортировка импортов (isort)

poetry run isort src/ tests/
Проверка PEP 8 (Flake8)

poetry run flake8 src/ tests/
Проверка типов (MyPy)

poetry run mypy src/
Запуск всех линтеров одной командой

poetry run black --check src/ tests/ && \
poetry run isort --check-only src/ tests/ && \
poetry run flake8 src/ tests/ && \
poetry run mypy src/
Загрузка из JSON
Поддерживается загрузка категорий и товаров из файла products.json:


from src.json_loader import load_categories_from_json

categories = load_categories_from_json("products.json")
Пример использования

from src.product import Product, Smartphone, LawnGrass
from src.category import Category

# Создание смартфона
phone = Smartphone(
    "iPhone 15", "512GB, Gray space", 210000.0, 8,
    98.2, "15", 512, "Gray space"
)

# Создание травы
grass = LawnGrass(
    "Газонная трава", "Элитная трава", 500.0, 20,
    "Россия", "7 дней", "Зеленый"
)

# Создание категории
category = Category("Смартфоны", "Высокотехнологичные смартфоны", [phone])

# Сложение (только одинаковые типы)
total = phone + phone  # Работает
# phone + grass  # TypeError!

# Добавление продукта в категорию
category.add_product(phone)  # Работает
# category.add_product("not a product")  # TypeError!

# Итерация по товарам
for product in ProductIterator(category):
    print(product)
Структура проекта

Project14_1/
├── src/
│   ├── __init__.py
│   ├── product.py           # Product, Smartphone, LawnGrass
│   ├── category.py          # Category
│   ├── json_loader.py       # Загрузка из JSON
│   └── product_iterator.py  # Итератор для товаров
├── tests/
│   ├── __init__.py
│   ├── test_product.py
│   ├── test_category.py
│   ├── test_smartphone.py
│   ├── test_lawn_grass.py
│   ├── test_product_magic.py
│   ├── test_json_loader.py
│   └── test_product_iterator.py
├── main.py                  # Демонстрационный скрипт
├── products.json            # Данные для загрузки
├── htmlcov/                 # HTML отчёт о покрытии
├── pyproject.toml           # Зависимости Poetry
├── .flake8                  # Конфиг Flake8
├── .gitignore
└── README.md
Автор
Владимир

Статус проекта
✅ Проект завершён. Все тесты проходят. Покрытие кода 100%.

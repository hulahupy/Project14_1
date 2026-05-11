# Project14_1 - Управление категориями и товарами

## Описание
Проект реализует систему управления товарами и категориями для интернет-магазина.  
Поддерживаются различные типы товаров: обычные продукты, смартфоны и газонная трава.

---

## 📚 Оглавление
- [Классы](#классы)
- [Абстрактный класс BaseProduct](#абстрактный-класс-baseproduct)
- [Миксин PrintInitMixin](#миксин-printinitmixin)
- [Класс Order (дополнительное задание)](#класс-order-дополнительное-задание)
- [Валидация количества товара](#валидация-количества-товара)
- [Средняя цена категории](#средняя-цена-категории)
- [Установка и запуск](#установка-и-запуск)
- [Тестирование](#тестирование)
- [Линтеры и форматирование](#линтеры-и-форматирование)
- [Структура проекта](#структура-проекта)

---

## Классы

### Product (базовый класс)
- `name` - название товара
- `description` - описание
- `price` - цена
- `quantity` - количество на складе

**Валидация:**
- При создании товара с `quantity <= 0` выбрасывается `ValueError` с сообщением  
  «Товар с нулевым количеством не может быть добавлен»

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
- `middle_price()` - возвращает среднюю цену всех товаров в категории (для пустой категории возвращает 0)
- `__str__` - строковое представление: `"Название, количество продуктов: X шт."`

### ProductIterator
Класс для итерации по товарам категории в цикле `for`.

---

## Абстрактный класс BaseProduct

Базовый абстрактный класс для всех продуктов. Определяет обязательные методы:


class BaseProduct(ABC):
    @abstractmethod
    def __str__(self) -> str: ...

    @abstractmethod
    def __add__(self, other: 'BaseProduct') -> float: ...
Наследники: Product, Smartphone, LawnGrass

Миксин PrintInitMixin
Класс-миксин, который при создании объекта выводит в консоль информацию о создании.


class PrintInitMixin:
    def __init__(self, *args, **kwargs):
        """Автоматический вывод информации о создании объекта"""
Пример вывода:


Product('Телефон', 'Смартфон', 50000.0, 10)
Smartphone('iPhone', 'Смартфон', 100000.0, 5, efficiency=95.5, model='15 Pro', memory=256, color='Black')
LawnGrass('Трава', 'Газонная', 500.0, 20, country='Россия', germination_period='7 дней', color='Зеленый')
Класс Order (дополнительное задание)
Представляет заказ на один товар.


class Order(BaseOrder):
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def total_price(self) -> float:
        return self.product.price * self.quantity
Валидация количества товара
При создании продукта с quantity <= 0 выбрасывается исключение:


try:
    product = Product("Бракованный товар", "Описание", 1000.0, 0)
except ValueError as e:
    print(e)  # "Товар с нулевым количеством не может быть добавлен"
Средняя цена категории
Метод middle_price() в классе Category возвращает среднюю цену всех товаров:


category = Category("Смартфоны", "Описание", [product1, product2, product3])
average = category.middle_price()  # (price1 + price2 + price3) / 3

empty_category = Category("Пустая", "Описание", [])
average_empty = empty_category.middle_price()  # 0.0
Установка и запуск
Требования
Python 3.10+

Poetry

Установка зависимостей

poetry install
Запуск демонстрационного скрипта

poetry run python main.py
Тестирование
Запуск всех тестов

poetry run pytest -v
Результаты тестирования
Всего тестов: 51

Все тесты успешны ✅

Покрытие кода: 100%

Проверка покрытия

poetry run pytest --cov=src --cov-report=term
Генерация HTML отчёта о покрытии

poetry run pytest --cov=src --cov-report=html
Отчёт сохраняется в папку htmlcov/.

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
Структура проекта

Project14_1/
├── src/
│   ├── __init__.py           # Экспорт модулей
│   ├── base_product.py       # Абстрактный класс BaseProduct
│   ├── product.py            # Product, Smartphone, LawnGrass
│   ├── category.py           # Category (с middle_price)
│   ├── mixin.py              # PrintInitMixin
│   ├── order.py              # Order, BaseOrder
│   ├── json_loader.py        # Загрузка из JSON
│   └── product_iterator.py   # Итератор для товаров
├── tests/
│   ├── __init__.py
│   ├── test_base_product.py
│   ├── test_product.py
│   ├── test_product_exceptions.py    # Тесты валидации
│   ├── test_product_magic.py
│   ├── test_category.py
│   ├── test_category_magic.py
│   ├── test_category_middle_price.py # Тесты middle_price
│   ├── test_smartphone.py
│   ├── test_lawn_grass.py
│   ├── test_json_loader.py
│   ├── test_product_iterator.py
│   ├── test_mixin.py
│   └── test_order.py
├── main.py                    # Демонстрационный скрипт
├── products.json              # Данные для загрузки
├── htmlcov/                   # HTML отчёт о покрытии
├── pyproject.toml             # Зависимости Poetry
├── .flake8                    # Конфиг Flake8
├── .gitignore
└── README.md

История версий
Версия	Что добавлено
1.0	Базовые классы Product и Category
2.0	Магические методы __str__, __add__
2.1	Классы-наследники Smartphone и LawnGrass
3.0	Абстрактный класс BaseProduct, миксин PrintInitMixin, класс Order
4.0	Валидация quantity в Product, метод middle_price в Category

## Автор
Владимир
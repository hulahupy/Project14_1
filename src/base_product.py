from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    def __init__(self, *args, **kwargs):
        """Конструктор базового класса — принимает любые аргументы для миксина"""
        super().__init__()

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: BaseProduct) -> float:
        pass

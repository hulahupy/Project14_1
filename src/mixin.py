class PrintInitMixin:
    """Миксин для вывода информации о создании объекта через __init__"""

    def __init__(self, *args, **kwargs):
        """Вывод информации о создании объекта при инициализации"""
        class_name = self.__class__.__name__
        params = []
        for arg in args:
            params.append(repr(arg))
        for key, value in kwargs.items():
            params.append(f"{key}={repr(value)}")
        print(f"{class_name}({', '.join(params)})")
        super().__init__(*args, **kwargs)

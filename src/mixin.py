class PrintInitMixin:
    """Миксин для вывода информации о создании объекта"""

    @staticmethod
    def print_init_info(instance, *args, **kwargs):
        """Печать информации о создании объекта"""
        class_name = instance.__class__.__name__
        params = [repr(arg) for arg in args]
        params.extend([f"{key}={repr(value)}" for key, value in kwargs.items()])
        print(f"{class_name}({', '.join(params)})")

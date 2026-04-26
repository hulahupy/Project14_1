import json
import tempfile

import pytest

from src.json_loader import load_categories_from_json


class TestJsonLoader:
    """Тесты для загрузки из JSON"""

    def test_load_categories_from_json(self):
        """Тест загрузки категорий из JSON"""
        test_data = [
            {
                "name": "Тестовая категория",
                "description": "Описание тестовой категории",
                "products": [
                    {"name": "Тестовый товар", "description": "Описание товара", "price": 1000.0, "quantity": 10}
                ],
            }
        ]

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(test_data, f, ensure_ascii=False)
            temp_path = f.name

        categories = load_categories_from_json(temp_path)

        assert len(categories) == 1
        assert categories[0].name == "Тестовая категория"
        assert len(categories[0].products) == 1
        assert categories[0].products[0].name == "Тестовый товар"

    def test_file_not_found(self):
        """Тест ошибки при отсутствии файла"""
        with pytest.raises(FileNotFoundError):
            load_categories_from_json("nonexistent_file.json")

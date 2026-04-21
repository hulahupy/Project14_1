import json
import tempfile

import pytest

from src.json_loader import load_categories_from_json


class TestJsonLoader:
    def test_load_categories_from_json(self):
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
        # Геттер products теперь возвращает строку, а не список
        assert "Тестовый товар" in categories[0].products
        assert "1000.0 руб." in categories[0].products
        assert "Остаток: 10 шт." in categories[0].products

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            load_categories_from_json("nonexistent.json")

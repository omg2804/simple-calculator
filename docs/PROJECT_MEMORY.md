# Project Memory

## Original Request
Create a simple calculator using python.

## Architecture Blueprint
{'project_name': 'SimpleCalculator', 'files': [{'path': 'src/models/calculator.py', 'purpose': 'Contains the Calculator class with basic arithmetic operations.', 'exports': ['Calculator'], 'imports_from': [], 'third_party_deps': [], 'model_schema': {'Calculator': {'fields': {'result': 'float'}}}, 'fields': {}}, {'path': 'src/interface/main.py', 'purpose': 'Main entry point for the calculator application.', 'exports': [], 'imports_from': ['src/models/calculator.py'], 'third_party_deps': [], 'model_schema': {}, 'fields': {}}], 'dependency_order': ['src/models/', 'src/interface/'], 'third_party_packages': []}

## Coding Rules
- Follow modular boundaries.
- Internal imports must be absolute (`src.*`).
- Keep type annotations and docstrings in generated code.

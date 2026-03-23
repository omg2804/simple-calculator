import pytest
from src.models.calculator import Calculator

class TestCalculator:
    def setup_method(self):
        self.calculator = Calculator()

    def test_add(self):
        assert self.calculator.add(1.0, 2.0) == 3.0
        assert self.calculator.add(-1.0, 1.0) == 0.0
        assert self.calculator.add(-1.0, -1.0) == -2.0

    def test_subtract(self):
        assert self.calculator.subtract(5.0, 2.0) == 3.0
        assert self.calculator.subtract(0.0, 1.0) == -1.0
        assert self.calculator.subtract(-1.0, -1.0) == 0.0

    def test_multiply(self):
        assert self.calculator.multiply(3.0, 2.0) == 6.0
        assert self.calculator.multiply(-1.0, 1.0) == -1.0
        assert self.calculator.multiply(0.0, 5.0) == 0.0

    def test_divide(self):
        assert self.calculator.divide(6.0, 2.0) == 3.0
        assert self.calculator.divide(-4.0, 2.0) == -2.0
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calculator.divide(1.0, 0.0)

    def test_end_to_end(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'add')
        monkeypatch.setattr('builtins.input', lambda _: '3')
        monkeypatch.setattr('builtins.input', lambda _: '4')
        assert self.calculator.add(3.0, 4.0) == 7.0
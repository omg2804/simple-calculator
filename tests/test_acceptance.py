import pytest
from src.models.calculator import Calculator

class TestCalculatorAcceptance:
    def setup_method(self):
        self.calculator = Calculator()

    def test_addition(self):
        assert self.calculator.add(1.0, 2.0) == 3.0
        assert self.calculator.add(-1.0, 1.0) == 0.0

    def test_subtraction(self):
        assert self.calculator.subtract(5.0, 2.0) == 3.0
        assert self.calculator.subtract(0.0, 1.0) == -1.0

    def test_multiplication(self):
        assert self.calculator.multiply(3.0, 2.0) == 6.0
        assert self.calculator.multiply(-1.0, 1.0) == -1.0

    def test_division(self):
        assert self.calculator.divide(6.0, 2.0) == 3.0
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calculator.divide(1.0, 0.0)

    def test_end_to_end_addition(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'add')
        monkeypatch.setattr('builtins.input', lambda _: '3')
        monkeypatch.setattr('builtins.input', lambda _: '4')
        assert self.calculator.add(3.0, 4.0) == 7.0

    def test_end_to_end_subtraction(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'subtract')
        monkeypatch.setattr('builtins.input', lambda _: '5')
        monkeypatch.setattr('builtins.input', lambda _: '2')
        assert self.calculator.subtract(5.0, 2.0) == 3.0

    def test_end_to_end_multiplication(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'multiply')
        monkeypatch.setattr('builtins.input', lambda _: '3')
        monkeypatch.setattr('builtins.input', lambda _: '4')
        assert self.calculator.multiply(3.0, 4.0) == 12.0

    def test_end_to_end_division(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'divide')
        monkeypatch.setattr('builtins.input', lambda _: '8')
        monkeypatch.setattr('builtins.input', lambda _: '2')
        assert self.calculator.divide(8.0, 2.0) == 4.0
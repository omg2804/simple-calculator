from dataclasses import dataclass, field
from typing import List

@dataclass
class CalculationHistory:
    operations: List[str] = field(default_factory=list)

    def add_operation(self, operation: str) -> None:
        if not operation:
            raise ValueError("Operation cannot be an empty string.")
        self.operations.append(operation)

    def get_history(self) -> List[str]:
        return self.operations

@dataclass
class Calculator:
    history: CalculationHistory

    def __init__(self):
        self.history = CalculationHistory()

    def add(self, a: float, b: float) -> float:
        result = a + b
        self.history.add_operation(f"Added {a} and {b}: {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self.history.add_operation(f"Subtracted {b} from {a}: {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self.history.add_operation(f"Multiplied {a} and {b}: {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history.add_operation(f"Divided {a} by {b}: {result}")
        return result

    def get_history(self) -> List[str]:
        return self.history.get_history()
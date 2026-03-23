from dataclasses import dataclass, field
from typing import List

@dataclass
class CalculationHistory:
    history: List[str] = field(default_factory=list)

    def add_entry(self, entry: str) -> None:
        if not entry:
            raise ValueError("Entry cannot be empty or None")
        self.history.append(entry)

    def get_history(self) -> List[str]:
        return self.history

    def clear_history(self) -> None:
        self.history.clear()
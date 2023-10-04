from typing import Optional, TypeVar, Generic
from dataclasses import dataclass


T = TypeVar('T')


@dataclass
class ClassA(Generic[T]):
    # optional information of any type
    info: Optional[T] = None
    alpha: float = 0.0

    def add(self, a: float) -> float:
        self.alpha += a
        return self.alpha

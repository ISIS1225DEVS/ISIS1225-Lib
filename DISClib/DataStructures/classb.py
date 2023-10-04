from typing import Optional, TypeVar, Generic
from dataclasses import dataclass


T = TypeVar('T')


@dataclass
class ClassB(Generic[T]):
    # optional information of any type
    info: Optional[T] = None
    beta: int = 0

    def add(self, b: int) -> int:
        self.beta += b
        return self.beta

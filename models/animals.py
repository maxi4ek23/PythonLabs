from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, weight: float):
        self._name = name
        self._weight = weight

    def __str__(self) -> str:
        return f"My name: {self._name}. My weight: {self._weight}. "

    @abstractmethod
    def who_are_u(self) -> str:
        pass

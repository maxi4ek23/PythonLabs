from models.animals import Animal


class Mammal(Animal):
    def __init__(self, name: str, weight: float, has_fur: bool, is_domestic: bool):
        super().__init__(name, weight)
        self.__has_fur = has_fur
        self.__is_domestic = is_domestic

    def __str__(self) -> str:
        return super().__str__() + f"Do I have fur? -{self.__has_fur}. Do I am domestic? -{self.__is_domestic}."

    def who_are_u(self) -> str:
        words = "Hello I am Mammal."
        return words

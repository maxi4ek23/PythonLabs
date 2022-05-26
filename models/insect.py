from models.animals import Animal


class Insect(Animal):
    def __init__(self, name: str, weight: float, count_of_legs: int, count_of_wings: int):
        super().__init__(name, weight)
        self.__count_of_legs = count_of_legs
        self.__count_of_wings = count_of_wings

    def __str__(self) -> str:
        return super().__str__() + f"I have {self.__count_of_legs} legs. I have {self.__count_of_wings} wings."

    def who_are_u(self) -> str:
        words = "Hello I am Insect."
        return words

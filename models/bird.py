from models.animals import Animal


class Bird(Animal):
    def __init__(self, name: str, weight: float, wing_size: int, can_fly: bool):
        super().__init__(name, weight)
        self.__wing_size = wing_size
        self.__can_fly = can_fly

    def __str__(self) -> str:
        return super().__str__() + f"My wing size: {self.__wing_size}. Can I fly? -{self.__can_fly}."

    def who_are_u(self) -> str:
        words = "Hello I am Bird."
        return words




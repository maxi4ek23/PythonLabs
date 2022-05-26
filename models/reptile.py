from models.animals import Animal


class Reptile(Animal):
    def __init__(self, name: str, weight: float, can_shed_skin: bool, can_lay_eggs: bool):
        super().__init__(name, weight)
        self.__can_shed_skin = can_shed_skin
        self.__can_lay_eggs = can_lay_eggs

    def __str__(self) -> str:
        return super().__str__() + f"Can I shed the skin? -{self.__can_shed_skin}. Can I lay eggs? -{self.__can_lay_eggs}."

    def who_are_u(self) -> str:
        words = "Hello I am Reptile."
        return words

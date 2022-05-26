from models.animals import Animal


class Fish(Animal):
    def __init__(self, name: str, weight: float, number_of_gills: int, lives_in_salt_water: bool):
        super().__init__(name, weight)
        self.__number_of_gills = number_of_gills
        self.__lives_in_salt_water = lives_in_salt_water

    def __str__(self) -> str:
        return super().__str__() + f"I have {self.__number_of_gills} gills. Do I live in salt water? -{self.__lives_in_salt_water}."

    def who_are_u(self) -> str:
        words = "Hello I am Fish."
        return words


from models.fish import Fish
from models.bird import Bird
from models.mammal import Mammal
from models.insect import Insect
from models.reptile import Reptile


def main() -> None:
    penguin = Bird("Kovalski", 12.4, 4, True)
    capitan = Bird("Shkiper", 33.4, 8, False)
    print(penguin.who_are_u(), penguin)
    print(capitan.who_are_u(), capitan)
    fishka = Fish("Cool", 12.6, 12, True)
    print(fishka.who_are_u(), fishka)
    panda_kung_fu = Mammal("Po", 55.6, True, False)
    print(panda_kung_fu.who_are_u(), panda_kung_fu)
    vzhyk = Insect("Vzhyk", 1.6, 12, 4)
    print(vzhyk.who_are_u(), vzhyk)
    crocodile = Reptile("Gena", 120, True, True)
    print(crocodile.who_are_u(), crocodile)




if __name__ == "__main__":
    main()

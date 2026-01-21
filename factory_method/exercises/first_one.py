from abc import ABC, abstractmethod
from enum import Enum

class SpaceShipType(Enum):
    MILLENIUMFALCON = "Millenium Falcon"
    SERENITY = "Serenity" 


class SpaceShip(ABC):

    def __init__(self, x: int, y: int, size: int, display_name: str, speed: float):
        self.x = x
        self.y = y
        self.size = size
        self.display_name = display_name
        self.speed = speed

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def attack(self):
        pass


class MilleniumFalcon(SpaceShip):

    def __init__(self, x: int, y: int, size: int, display_name: str, speed: float):
        super().__init__(x, y, size, display_name, speed)

    def move(self):
        self.x += self.speed

    def attack(self):
        print("Pew pew! 🚀")

class Serenity(SpaceShip):

    def __init__(self, x: int, y: int, size: int, display_name: str, speed: float):
        super().__init__(x, y, size, display_name, speed)
    
    def move(self):
        self.y += self.speed

    def attack(self):
        print("KATCHAU")


class SpaceShipFactory:
    
    @staticmethod
    def create_space_ship(context):
        if context.space_ship_type == SpaceShipType.MILLENIUMFALCON:
            return MilleniumFalcon(context.x, context.y, context.size, context.display_name, context.speed)
        elif context.space_ship_type == SpaceShipType.SERENITY:
            return Serenity(context.x, context.y, context.size, context.display_name, context.speed)
          


class SpaceShipContext:
    def __init__(self, space_ship_type, x: int, y: int, size: int, display_name: str, speed: float):
        self.space_ship_type = space_ship_type
        self.x = x
        self.y = y
        self.size = size
        self.display_name = display_name
        self.speed = speed
        

if __name__ == "__main__":

    # Criando contexto para Millenium Falcon
    falcon_context = SpaceShipContext(
        space_ship_type=SpaceShipType.MILLENIUMFALCON,
        x=0,
        y=0,
        size=10,
        display_name="Millenium Falcon",
        speed=5.0
    )

    falcon = SpaceShipFactory.create_space_ship(falcon_context)

    print(f"Ship: {falcon.display_name}")
    print(f"Initial position: ({falcon.x}, {falcon.y})")

    falcon.move()
    falcon.attack()

    print(f"After move: ({falcon.x}, {falcon.y})")
    print("-" * 40)

    # Criando contexto para Serenity
    serenity_context = SpaceShipContext(
        space_ship_type=SpaceShipType.SERENITY,
        x=0,
        y=0,
        size=12,
        display_name="Serenity",
        speed=3.0
    )

    serenity = SpaceShipFactory.create_space_ship(serenity_context)

    print(f"Ship: {serenity.display_name}")
    print(f"Initial position: ({serenity.x}, {serenity.y})")

    serenity.move()
    serenity.attack()

    print(f"After move: ({serenity.x}, {serenity.y})")

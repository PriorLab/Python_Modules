class Plant:
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 ) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            self.height = height
            print(f"Height updated: {self.height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self.age = age
            print(f"Age updated: {self.age} days\n")

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.age


def create_plants() -> list[Plant]:
    return [
        Plant("Rose", 15, 10),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]


def display(plant: Plant) -> None:
    print("=== Garden Security System ===\n")
    print(f"Plant created: {plant.show()}")


if __name__ == "__main__":
    plant = create_plants()[0]
    display(plant)
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-25)
    plant.set_age(-30)
    print(f"\nCurrent state: {plant.show()}")

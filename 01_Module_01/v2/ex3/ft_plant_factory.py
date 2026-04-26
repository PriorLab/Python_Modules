class Plant:
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 ) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def create_plants() -> list[Plant]:
    return [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Oak", 30, 200),
        Plant("Fern", 120, 15),

    ]


def display(plants: list[Plant]) -> None:
    print("=== Plant Factory Output ===\n")
    for plant in plants:
        plant.show()
    print("\n======== All plants =========")


if __name__ == "__main__":
    plants = create_plants()
    display(plants)

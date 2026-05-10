class Plant:
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 growth: float
                 ) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self):
        self.height = self.height + self.growth

    def age_one_day(self):
        self.age += 1


def create_plants() -> list[Plant]:
    return [
        Plant("Rose", 24.2, 30, 0.8),
        Plant("Sunflower", 80, 45, 1.5),
        Plant("Cactus", 15, 120, 0.3),
    ]


def aging(plant: Plant, days: int) -> None:
    print("=== Garden Plant Growth ===\n")
    i = 1
    while i <= 7:
        print(f"=== Day {i} ===")
        i += 1
        plant.grow()
        plant.age_one_day()
        plant.show()
    total_growth = (days) * plant.growth
    print(f"\nGrowth this week: {total_growth:.0f}cm")
    print("\n=== Finishing Garden Growth ===")


if __name__ == "__main__":
    plant = create_plants()[0]
    aging(plant, 7)

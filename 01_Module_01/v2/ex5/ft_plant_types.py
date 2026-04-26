class Plant:
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 ) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.age} days old"


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, col: str) -> None:
        super().__init__(name, height, age)
        self.colour = col
        self.has_bloomed = False

    def bloom_flower(self) -> None:
        self.has_bloomed = True
        print("[asking the rose to bloom]")
        print(self)
        print(f"Color: {self.colour}")
        print("Rose is blooming beautifully!")

    def show_flower(self) -> None:
        print("=== Flower")
        print(self)
        print("Rose has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, tru: float) -> None:
        super().__init__(name, height, age)
        self.trunk = tru

    def shade_tree(self) -> None:
        print("[asking the oak to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self.height:.1f}cm "
            f"long and {self.trunk:.1f}cm wide."
        )

    def show_tree(self) -> None:
        print("\n=== Tree")
        print(self)
        print(f"Trunk diameter: {self.trunk:.1f}")


class Vegetable(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 season: str,
                 nutritional_value: int,
                 grow: float) -> None:
        super().__init__(name, height, age)
        self.season = season
        self.nutritional_value = nutritional_value
        self.growth_rate = grow

    def age_and_grow(self, days_growing: int):
        nutrition = self.nutritional_value
        print(f"Nutritional value: {nutrition}")
        nutrition = self.nutritional_value + days_growing
        self.height += self.growth_rate * days_growing
        self.age += days_growing
        print(f"[make tomato grow and age for {days_growing} days]")
        print(self)
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {nutrition}")

    def show_veggies(self) -> None:
        print("\n=== Vegetable")
        print(self)
        print(f"Harvest season: {self.season}")


def main() -> None:
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 15, 10, "red")
    rose.show_flower()
    rose.bloom_flower()

    oak = Tree("Oak", 200, 365, 5)
    oak.show_tree()
    oak.shade_tree()

    tomato = Vegetable("Tomato", 5, 10, "April", 0, 2.1)
    tomato.show_veggies()
    tomato.age_and_grow(20)


if __name__ == "__main__":
    main()

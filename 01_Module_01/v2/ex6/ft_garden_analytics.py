class Stats:
    def __init__(self) -> None:
        self._grow_calls = 0
        self._age_calls = 0
        self._show_calls = 0

    def add_grow_call(self) -> None:
        self._grow_calls += 1

    def add_age_call(self) -> None:
        self._age_calls += 1

    def add_show_call(self) -> None:
        self._show_calls += 1

    def display_stats(self) -> None:
        print(
            f"Stats: {self._grow_calls} grow, "
            f"{self._age_calls} age, "
            f"{self._show_calls} show"
        )


class Plant(Stats):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
    ):
        super().__init__()
        self.name = name
        self.height = height
        self.age = age

    def growth(self, growth: float) -> None:
        self.height += growth
        self.add_grow_call()

    def older(self, days: int) -> None:
        self.age += days
        self.add_age_call()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self.add_show_call()

    @staticmethod
    def year_old(age: int) -> None:
        print(f"Is {age} days more than a year? -> {age > 365}")


class Flower(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 color: str,
                 bloom: bool = False
                 ):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = bloom

    def bloom_state(self) -> None:
        if self.bloom is False:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully")

    def ask_to_bloom_grow(self) -> None:
        print("[asking the rose to grow and bloom]")
        self.bloom = True
        self.growth(8.0)


class Tree(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 trunk: float,
                 shade: int = 0):
        super().__init__(name, height, age)
        self.trunk = trunk
        self.shade = shade

    def display_shade(self):
        print(f"{self.shade} shade")

    def produce_shade(self):
        self.shade += 1
        print(
            f"[asking the {self.name} to produce shade]\n"
            f"Tree {self.name} now produces a shade of {self.height}cm"
            f" long and {self.trunk}cm wide."
        )


class Seed(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int,
                 color: str,
                 seeds: int = 0,
                 bloom: int = 0):
        super().__init__(name, height, age)
        self.color = color
        self.seeds = seeds
        self.bloom = bloom

    def seed_status(self):
        if self.bloom != 0:
            print(f"Color: {self.color}")
            print(f"{self.name} is blooming beautifully!")
            print(f"Seeds: {self.seeds}")
        else:
            print(f"Color: {self.color}")
            print(f"{self.name} has not bloomed yet")
            print(f"Seeds: {self.seeds}")

    def seed_age_grow_bloom(self):
        print("[make sunflower grow, age and bloom]")
        self.height += 30
        self.age += 20
        self.seeds = 42
        self.bloom = 1
        self.add_age_call()
        self.add_grow_call()


class anonymous(Plant):
    def __init__(self,
                 name: str,
                 height: float,
                 age: int):
        super().__init__(name, height, age)


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.year_old(30)
    Plant.year_old(400)
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print(f"Color: {rose.color}")
    rose.bloom_state()
    print(f"[statistics for {rose.name}]")
    rose.display_stats()
    rose.ask_to_bloom_grow()
    rose.show()
    print(f"Color: {rose.color}")
    rose.bloom_state()
    print(f"[statistics for {rose.name}]")
    rose.display_stats()

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"Trunk diameter: {oak.trunk:.1f}cm")
    print(f"[statistics for {oak.name}]")
    oak.display_stats()
    oak.display_shade()
    oak.produce_shade()
    print(f"[statistics for {oak.name}]")
    oak.display_stats()
    oak.display_shade()

    print()
    print("=== Seed")
    Sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    Sunflower.show()
    Sunflower.seed_status()
    Sunflower.seed_age_grow_bloom()
    Sunflower.show()
    Sunflower.seed_status()
    print(f"[statistics for {Sunflower.name}]")
    Sunflower.display_stats()

    print()
    print("=== Anonymous")
    unknown = anonymous("Unknown", 0.0, 0)
    unknown.show()
    print(f"[statistics for {unknown.name} plant]")
    unknown.display_stats()


if __name__ == "__main__":
    main()

class Plant:
    class Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self):
            self._grow_calls += 1

        def add_age(self):
            self._age_calls += 1

        def add_show(self):
            self._show_calls += 1

        def display(self):
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self):
        self.height += 2.1
        self._stats.add_grow()

    def age_one_day(self, days=1):
        self.age += days
        self._stats.add_age()

    def show(self):
        self._stats.add_show()
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def display_stats(self):
        self._stats.display()


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def bloom(self):
        self.has_bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def add_shade(self):
            self._shade_calls += 1

        def display(self):
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree.TreeStats()

    def produce_shade(self):
        self._stats.add_shade()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Seed(Flower):
    def __init__(self, name, height, age, color, seeds):
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def display_plant_statistics(plant):
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


print("=== Garden statistics ===")

print("=== Check year-old")
print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

print("=== Flower")
rose = Flower("Rose", 15.0, 10, "red")
rose.show()
display_plant_statistics(rose)
print("[asking the rose to grow and bloom]")
rose.grow()
rose.bloom()
rose.show()
display_plant_statistics(rose)

print("=== Tree")
oak = Tree("Oak", 200.0, 365, 5.0)
oak.show()
display_plant_statistics(oak)
print("[asking the oak to produce shade]")
oak.produce_shade()
display_plant_statistics(oak)

print("=== Seed")
sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
sunflower.show()
print("[make sunflower grow, age and bloom]")
sunflower.grow()
sunflower.age_one_day(20)
sunflower.bloom()
sunflower.show()
display_plant_statistics(sunflower)

print("=== Anonymous")
unknown = Plant.anonymous()
unknown.show()
display_plant_statistics(unknown)
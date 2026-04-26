class Stats:
    def __init__(self) -> None:
        self._grow_calls = 0
        self._age_calls = 0
        self._show_calls = 0

    def add_grow_call(self) -> None:
        self._grow_calls += 1

    def add_age_call(self) -> None:
        self._age_calls += 1

    def add
class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
    ):
        self.name = name
        self.height = height
        self.age = age

    def growth(self, growth: float) -> None:
        self.height += growth

    def older(self, days:int) -> None:
        self.age += days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

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

    



def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")

    Plant.year_old(30)
    Plant.year_old(400)
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()


if __name__ == "__main__":
    main()

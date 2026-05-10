class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def check_plant(plant_name: str, is_wilting: bool) -> None:

    if is_wilting:
        raise PlantError(f"The  {plant_name} plant is wilting!")


def check_water(no_water: bool) -> None:
    if no_water:
        raise WaterError(
            "Not enough water in the tank!"
        )


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant("tomato", True)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water(True)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(True)
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()

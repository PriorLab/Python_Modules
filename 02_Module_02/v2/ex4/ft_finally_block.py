class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
        return

    raise PlantError(
        f"Invalid plant name to water: '{plant_name}'"
        "\n.. ending tests and returning to main"
    )


def test_watering_system(garden: list[str]) -> None:
    print("Opening watering system")
    is_error: bool = False
    try:
        for plant in garden:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        is_error = True
    finally:
        print("Closing watering system\n")
    if is_error:
        return


if __name__ == "__main__":

    plants1 = ["Tomato", "Lettuce", "Carrots"]
    plants2 = ["Tomato", "lettuce", "Carrots"]
    print("=== Garden Watering System ===\n")
    print("Testing valid plants...")
    test_watering_system(plants1)
    print("Testing invalid plants...")
    test_watering_system(plants2)
    print("Cleanup always happens, even with errors!")

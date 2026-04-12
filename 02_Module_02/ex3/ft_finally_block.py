class PlantError(Exception):
    pass

def water_plant(plant_name: str) -> None:
    if not plant_name[0].isupper():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")

def test_watering_system(plants: list[str]) -> None:
    print('Opening watering system')
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print('.. ending tests and returning to main')
        return
    finally:
        print('Closing watering system')
        
def main() -> None:

    print('=== Garden Watering System ===')
    print('Testing valid plants...')
    test_watering_system(['Tomato','Lettuce','Carrots'])
    print('Testing invalid plants...')
    test_watering_system(['Tomato','lettuce','Carrots'])
    print('Cleanup always happens, even with errors!')

if __name__ == "__main__":
    main()



#=== Garden Watering System ===
#Testing valid plants...
#Opening watering system
#Watering Tomato: [OK]
#Watering Lettuce: [OK]
#Watering Carrots: [OK]
#Closing watering system
#Testing invalid plants...
#Opening watering system
#Watering Tomato: [OK]
#Caught PlantError: Invalid plant name to water: 'lettuce'
#.. ending tests and returning to main
#Closing watering system
#Cleanup always happens, even with errors!
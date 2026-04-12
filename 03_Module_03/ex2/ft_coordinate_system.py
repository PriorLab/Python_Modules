import math

def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z':")

        coordinates = user_input.split(',')

        if len(coordinates) != 3:
            print("Invalid Syntax")
            continue
        
        final_coordinates = []

        try:
            for x in coordinates:
                value = float(x.strip())
                final_coordinates.append(value)
            return tuple(final_coordinates)
        
        except ValueError as e:
            for x in coordinates:
                try:
                    float(x.strip())
                except ValueError:
                    print(f"Error on parameter '{x.strip()}': {e}")
                    break
def distance_3d(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> float:
    return math.sqrt(
        (point2[0] - point1[0]) ** 2 +
        (point2[1] - point1[1]) ** 2 +
        (point2[2] - point1[2]) ** 2
    )

def main() -> None:
    print('=== Game Coordinate System ===')
    print('Get a first set of coordinates')
    first_coordinates = get_player_pos()
    print(f"Got a first tuple: {first_coordinates}")
    print(f"It includes: X={first_coordinates[0]}, Y={first_coordinates[1]}, Z={first_coordinates[2]}")
    center  = (0.0,0.0,0.0)
    center_distance = distance_3d(first_coordinates, center)
    print(f"Distance to center: {center_distance:.4f}")
    print('\nGet a second set of coordinates')
    second_coordinates = get_player_pos()
    coordinates_distance = distance_3d(first_coordinates, second_coordinates)
    print(f"Distance between the 2 sets of coordinates: {coordinates_distance:.4f}")

if __name__ == "__main__":
    main()



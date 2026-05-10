#!/usr/bin/python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        coord = user_input.split(",")
        if len(coord) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(coord[0].strip())
            y = float(coord[1].strip())
            z = float(coord[2].strip())
            return (x, y, z)
        except ValueError as e:
            for part in coord:
                try:
                    float(part.strip())
                except ValueError:
                    print(f"Error on parameter '{part.strip()}: {e}")
                    break


def d_to_center_calculus(
        coord1: tuple[float, float, float], coord2: tuple[float, float, float]
) -> float:
    x1 = coord1[0]
    y1 = coord1[1]
    z1 = coord1[2]
    x2 = coord2[0]
    y2 = coord2[1]
    z2 = coord2[2]
    return (float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)))


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    coord0 = (0.0, 0.0, 0.0)
    coord1 = get_player_pos()
    print(f"Got a first tuple: {coord1}")
    print(f"It includes: X={coord1[0]}, Y={coord1[1]}, Z={coord1[2]}")
    d_to_center1 = d_to_center_calculus(coord0, coord1)
    print(f"Distance to center: {d_to_center1:.4f}\n")

    print("Get a second set of coordinates")
    coord2 = get_player_pos()
    d_to_center2 = d_to_center_calculus(coord1, coord2)
    print(f"Distance to center: {d_to_center2:.4f}\n")

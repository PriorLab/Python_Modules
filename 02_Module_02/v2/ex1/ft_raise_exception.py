def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(
            f"{temp}°C is too cold for plants (min 0°C)"
        )
    if temp > 40:
        raise ValueError(
            f"{temp}°C is too hot for plants (max 40°C)"
        )
    return temp


def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(input_temperature(temp_str))
        print(f"Temperature is now {temp}\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")


def main() -> None:
    print("=== Garden Temperature ===\n")

    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()

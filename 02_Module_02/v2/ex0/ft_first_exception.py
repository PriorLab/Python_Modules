def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    print("Input data is '25'")
    try:
        temp = int(input_temperature("25"))
        print(f"Temperature is now {temp}\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    print("Input data is 'abc'")
    try:
        temp = int(input_temperature("abc"))
        print(f"Temperature is now {temp}\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

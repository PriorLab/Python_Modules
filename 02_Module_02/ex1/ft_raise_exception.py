def input_temperature(temp_str) -> int:
    temp = int(temp_str)

    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    print("Input data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("Input data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("Input data is '100'")
    try:
        temp = input_temperature("100")
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    
    print("Input data is '-50'")
    try:
        temp = input_temperature("-50")
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()